FROM ubuntu:18.10

RUN apt-get update -y && \
    apt-get install -y wget -q && \
    apt-get install -y python3-pip python3-dev && \
    apt-get install -y nginx uwsgi uwsgi-plugin-python3 && \
    apt-get install -y vim

RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy

ENV GOOGLE_APPLICATION_CREDENTIALS="/gcloud-stuff/application_default_credentials.json"
ENV DATABASE_URL="postgresql://postgres:postgres@/yogi?host=/cloudsql/saas-rally-dev:us-west2:yogi-berra"
ENV APP_SECRET="whitershadeofpale"

RUN mkdir -p /cloudsql/saas-rally-dev:us-west2:yogi-berra && \
     chmod 777 /cloudsql && \
     chmod 777 /cloudsql/saas-rally-dev:us-west2:yogi-berra

COPY ./requirements.txt /requirements.txt
COPY ./nginx.conf /etc/nginx/nginx.conf

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

RUN adduser --disabled-password --gecos '' nginx\
  && chown -R nginx:nginx /app \
  && chmod 777 /run/ -R

ENTRYPOINT [ "/bin/bash", "/launcher.sh"]