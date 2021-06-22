#!/usr/bin/env python3
import sqlite3

class Database():
    """ database class"""
    def __init__(self):
        self.conn = sqlite3.connect("pages.db")
        self.c = self.conn.cursor()

    def create_about(self):
        """ start db from nothing"""
        with self.conn:
            self.c.execute("""CREATE TABLE about (
                name integer,
                title text,
                p1 text,
                p2 text
                ) """)

    def insert_about(self):
        """ insert into about table"""
        insert1 = {'name': 1, 'title': 'StoneCo. Downflo', 'p1': 'We are a family owned and operated do it all construction company providing service to the Collinsville & Greater Tulsa Area. We believe in giving back to the community that we live in, and strive for all of our clients to become like family!', 'p2': 'NONE'}
        insert2 = {'name': 2, 'title': 'StoneCo. Downflo', 'p1': 'We are a family owned and operated do it all construction company providing service to the Collinsville & Greater Tulsa Area. We believe in giving back to the community that we live in, and strive for all of our clients to become like family!', 'p2': 'We are a family owned and operated do it all construction company providing service to the Collinsville & Greater Tulsa Area. We believe in giving back to the community that we live in, and strive for all of our clients to become like family!'}
        insert3 = {'name': 3, 'title': 'StoneCo. Downflo', 'p1': 'We are a family owned and operated do it all construction company providing service to the Collinsville & Greater Tulsa Area. We believe in giving back to the community that we live in, and strive for all of our clients to become like family!', 'p2': 'We are a family owned and operated do it all construction company providing service to the Collinsville & Greater Tulsa Area. We believe in giving back to the community that we live in, and strive for all of our clients to become like family!'}
        with self.conn:
            self.c.execute("INSERT INTO about VALUES (:name, :title, :p1, :p2)", insert1)
            self.c.execute("INSERT INTO about VALUES (:name, :title, :p1, :p2)", insert2)
            self.c.execute("INSERT INTO about VALUES (:name, :title, :p1, :p2)", insert3)

    def update_all_about(self, update):
        """update about table"""
        with self.conn:
            self.c.execute("UPDATE about SET title=:title, p1=:p1, p2=:p2 WHERE name=:name", update)

    def update_title_about(self, title):
        """update about table"""
        with self.conn:
            self.c.execute("UPDATE about SET title=:title WHERE name=:name", title)

    def update_p1_about(self, p):
        """update about table"""
        with self.conn:
            self.c.execute("UPDATE about SET p1=:p1 WHERE name=:name", p)

    def update_p2_about(self, p):
        """update about table"""
        with self.conn:
            self.c.execute("UPDATE about SET p2=:p2 WHERE name=:name", p)

    def get_about(self):
        """print about table"""
        with self.conn:
            self.c.execute("SELECT * FROM about")
            return self.c.fetchall()

    def close(self):
        """ close connection"""
        self.conn.close()
