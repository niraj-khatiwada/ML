# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import psycopg2

class ImdbPipeline(object):

    def open_spider(self, spider):
        #Setup PG connection
        logging.warning("****************SPIDER OPENED*****************")
        self.conn = psycopg2.connect(
            host = "localhost",
            dbname = "snorlex",
            user = "postgres",
            password = "_sn0r13xpl"
        )
        #Setup cursor
        self.cur = self.conn.cursor()
        try:
            self.cur.execute('''
                CREATE TABLE best_movies (
                    ID SERIAL PRIMARY KEY,
                    Title VARCHAR(100),
                    Genre VARCHAR(100),
                    Released_Date VARCHAR(100),
                    Runtime VARCHAR(100),
                    Rating FLOAT
                );

            ''')
        except psycopg2.errors.DuplicateTable:
            pass 
        #Commit the query 
        self.conn.commit()

    def process_item(self, item, spider):
        self.cur.execute(
            f"INSERT INTO best_movies(Title, Genre, Released_Date, Runtime, Rating) VALUES(%s, %s, %s, %s, %s);", (item.get("Title"),item.get("Genre"),item.get("Released_Date"),item.get("Runtime"),item.get("Rating"),)
            )
        self.conn.commit()
        return item

    def close_spider(self, spider):
        #Close Transaction
        self.cur.close()
        #Close COnnection
        self.conn.close()
        logging.warning("******SPIDER CLOSED***************")

