import pymysql
from datetime import datetime

conn = pymysql.connect(host='remotemysql.com', port=3306, user='eCiPNxZhD1', password='LsyRZQfzqo', db='eCiPNxZhD1')
cursor = conn.cursor()
conn.autocommit(True)


def get_name(user_id):
    cursor.execute("SELECT * FROM eCiPNxZhD1.users WHERE id = %s", user_id)
    data = cursor.fetchall()

    if len(data) == 0:
        raise "ID does not exist"
    return data[0][1]


def add_user(user_id, name):
    now = get_time()
    data = [(user_id, name, now)]
    insert_statement = "INSERT INTO users (id,name,creation_date) values(%s,%s,%s)"
    cursor.executemany(insert_statement, data)


def update_user(user_id, new_name):
    if get_name(user_id):
        params = {'name': new_name, 'user_id': user_id}
        cursor.execute("UPDATE eCiPNxZhD1.users SET name = %(name)s WHERE id = %(user_id)s", params)
    else:
        raise "ID does not exist"


def delete_user(user_id):
    if get_name(user_id):
        cursor.execute("DELETE FROM eCiPNxZhD1.users WHERE id = %s", user_id)
    else:
        raise "ID does not exist"


def clean_db():
    cursor.execute("TRUNCATE TABLE users")


def get_time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

