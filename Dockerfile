FROM quay.io/rallysoftware/centos:stable
USER root
RUN rpm --rebuilddb
RUN yum update -y; yum clean all

RUN yum install -y wget --quiet

RUN yum groupinstall -y "development tools"
RUN yum install -y libffi-devel
RUN yum install -y zlib-devel bzip2-devel openssl-devel expat-devel

RUN wget http://python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
RUN tar xf Python-3.7.3.tar.xz
WORKDIR Python-3.7.3
RUN ./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
RUN make && make altinstall

RUN yum install -y epel-release
RUN yum install -y nginx
RUN yum install -y vim

WORKDIR /

RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy

ENV TEMPLATE_DATABASE_URL="postgresql://{db_user}:{db_password}@/{db_name}?host=/cloudsql/{gcp_project}:{gcp_zone}:{gcloud_sql_instance}"

RUN mkdir -p /cloudsql/saas-rally-dev:us-west2:yogi-berra && \
     chmod 777 /cloudsql && \
     chmod 777 /cloudsql/saas-rally-dev:us-west2:yogi-berra

COPY ./requirements.txt /requirements.txt
COPY ./nginx.conf /etc/nginx/nginx.conf

WORKDIR /

RUN pip3.7 install -r requirements.txt

COPY . /
COPY tls_start.sh /home/service/tls_start.sh

RUN chown -R nginx:nginx /gcloud-stuff
RUN chmod 777 //gcloud-stuff/ -R
RUN chown -R nginx:nginx /app
RUN chmod 777 /run/ -R
RUN chmod 755 /cloud_sql_proxy

USER nginx
ENTRYPOINT [ "/bin/bash", "/home/service/tls_start.sh"]