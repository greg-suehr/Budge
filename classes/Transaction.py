import sqlite3

class Transaction():
    def __init__(self, date, inflow, outflow, description, memo="", category=""):
        """Date, inflow, outflow, and description are required fields"""
        for field, value in [("date", date), ("inflow", inflow), ("outflow", outflow), ("description", description)]:
            if value == "": 
                print("%s is a required field." % field) 
                return
        self.date = date
        self.inflow = inflow
        self.outflow = outflow
        self.description = description
        self.memo = memo
        self.category = category 
        

    def create(self):
        """Write a new transaction row to the database"""
        conn = sqlite3.connect('budge.db') # TODO: use an existing connection?
        c = conn.cursor()
        c.execute('INSERT INTO transactions (date, inflow, outflow, description, memo, category_id)'
                  'VALUES ("%s", "%s", "%s", "%s", "%s", "%s")' % (self.date, self.inflow, self.outflow, self.description, self.memo, self.category))
        conn.commit()
