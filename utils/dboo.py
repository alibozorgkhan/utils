# -*- coding: utf-8 -*-

import psycopg2
import settings

from psycopg2 import extras


class Cursor:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.cursor = self.db.cursor(cursor_factory=extras.RealDictCursor)
        return self.cursor

    def __exit__(self, type, value, traceback):
        self.cursor.close()


class DB:
    def __init__(self):
        connection_config = []
        for k, v in settings.POSTGRES_CONFIG.iteritems():
            connection_config.append("%s='%s'" % (k, v))

        db = psycopg2.connect(" ".join(connection_config))
        self.cursor = Cursor(db)

    def read(self, query, just_one=False):
        res = None
        with self.cursor as cursor:
            cursor.execute(query)
            if just_one:
                res = cursor.fetchone()
            else:
                res = cursor.fetchall()
        return res

    def write(self, query):
        with self.cursor as cursor:
            cursor.execute(query)
            self.db.commit()
