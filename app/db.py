import mysql.connector
import settings
from mysql.connector import errorcode
from schema import TABLES
from log import get_log


def get_db():
    cnx = mysql.connector.connect(**settings.mysql_config)
    cursor = cnx.cursor()
    return cursor, cnx


# def create_schema():
#     cursor, cnx_mysql = get_db()
#     my_logger = get_log()

#     for table_name in TABLES:
#         table_description = TABLES[table_name]
#         try:
#             print("Creating table {}: ".format(table_name), end='')
#             cursor.execute(table_description)
#         except mysql.connector.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 my_logger.warning("Table already exists: {}".format(TABLES[table_name]))
#             else:
#                 my_logger.error(err.msg)
#         else:
#             print("OK")

#     cursor.close()
#     cnx_mysql.close()
