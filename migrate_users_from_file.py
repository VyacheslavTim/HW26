import json
import sqlite3


def migrate():
    with open('users.json') as file:
        users = json.load(file)

    insert_values = ','.join([f"('{user['username']}', '{user['password']}')" for user in users])

    with sqlite3.connect('instance/test.db') as conn:
        conn.execute(
            f"""
            INSERT INTO "user" ("username", "password")
            VALUES {insert_values}
            """
        )


if __name__ == '__main__':
    migrate()
