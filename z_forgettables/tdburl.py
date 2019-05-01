import os


def dburl(template):
    replaceables = ['db_user', 'db_password', 'db_name', 'gcp_project', 'gcp_zone', 'gcloud_sql_instance']
    environ_vars = ['DB_USER', 'DB_PASSWORD', 'DB_NAME', 'PROJECT_ID',  'GCP_ZONE', 'GCLOUD_SQL_INSTANCE']
    result = template
    for target, jewel in zip(replaceables, environ_vars):
        result = result.replace("{%s}" % target, os.getenv(jewel))
    return result

result = dburl(os.getenv('TEMPLATE_DATABASE_URL'))
print(result)
good = "postgresql://postgres:postgres@/yogi?host=/cloudsql/saas-rally-dev:us-west2:yogi-berra"
assert result == good