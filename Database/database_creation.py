import psycopg2 
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def database_creation(database_name):
    try:
        connection = psycopg2.connect(
            user = 'postgres',
            password = 'superuser1604',
            host = '::1',
            port = '5432'
            )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        sql_create_database = f'CREATE DATABASE {database_name}'
        cursor.execute(sql_create_database)
        print('База данных успешно создана')

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
            
            
def database_column_delete(table_name, column_name):
    try:
        connection = psycopg2.connect(
            database = 'to_do_list_db',
            user = 'postgres',
            password = 'superuser1604',
            host = '::1',
            port = '5432'
            )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        sql_delete_column = f'ALTER TABLE {table_name} DROP COLUMN {column_name}'
        cursor.execute(sql_delete_column)
        print('Столбец успешно удален')

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

database_column_delete('userssssss', "password")
# database_creation('to_do_list_db')
