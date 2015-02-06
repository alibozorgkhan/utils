# -*- coding: utf-8 -*-

import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DB:
    def __init__(self):
        engine = create_engine('postgresql://' + settings.POSTGRES_CONFIG['user'] + ':' \
                                               + settings.POSTGRES_CONFIG['password'] + '@' \
                                               + settings.POSTGRES_CONFIG['host'] + '/' \
                                               + settings.POSTGRES_CONFIG['dbname'])
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def read(self, query, params={}, one=False):
        res = self.session.execute(query, params)
        self.session.commit()
        return res.fetchone() if one else res.fetchall()

    def read_in_chunks(self, query, params={}, chunk_size=1000):
        res = self.session.connection().execution_options(stream_results=True).execute(query, params)
        while True:
            rows = res.fetchmany(chunk_size)
            if rows:
                yield rows
            else:
                break

    def write(self, query, params={}):
        try:
            self.session.execute(query, params)
            self.session.commit()
        except:
            self.session.rollback()
