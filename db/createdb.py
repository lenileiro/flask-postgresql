import os
from psycopg2 import connect
from datetime import datetime
from flask import current_app


def connect_to_db(config=None):
    db_name = current_app.config.get('DATABASE_URI')
    return connect(db_name)


def init_db(config=None):

    conn = connect_to_db(config=config)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    print('Database created successfully')


if __name__ == '__main__':
    init_db()
