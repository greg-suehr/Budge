# Budge

Budge is a lightweight budgeting application that lives in your browser.



## Schema files

Budge is build on a sqlite3 database.

Schema files are a custom YAML file consumed by [script name] to initialize
a Budge database, like so:
  > python3 scripts/build_database.py

Datatypes (https://www.sqlitetutorial.net/sqlite-data-types/):
  - NULL
  - INTEGER
  - REAL
  - TEXT
  - BLOB