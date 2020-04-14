import sqlite3

class Period:
    def __init__(self, name):
        self.name = name

    def create(self):
        raise NotImplementedError

