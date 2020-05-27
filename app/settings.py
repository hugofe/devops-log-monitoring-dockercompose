from os import environ

mysql_config={
    'user': environ['MYSQL_DATABASE_USER'],
    'password': environ['MYSQL_DATABASE_PASSWORD'],
    'host': environ['MYSQL_DATABASE_HOST'],
    # 'database': environ['MYSQL_DBNAME']
}