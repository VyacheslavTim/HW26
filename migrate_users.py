import json

import psycopg2

from config import Config


def migrate():
    print('Started migration of users')
    with open('users.json') as file:
        users = json.load(file)

    insert_values = ','.join([f"('{user['username']}', '{user['password']}')" for user in users])

    with psycopg2.connect(Config.SQLALCHEMY_DATABASE_URI) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"""
                    INSERT INTO "user" ("username", "password")
                    VALUES {insert_values} ON CONFLICT DO NOTHING
                    """
            )

    print('Users migration completed')
