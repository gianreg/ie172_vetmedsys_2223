import dbconnect as db
from datetime import datetime

def addfewowners():
   
    sqlcode = """ INSERT INTO owners (
        owner_name,
        owner_modified_on
        )
    VALUES (%s, %s)"""
  

    db.modifydatabase(sqlcode, ['Gian Regollo', datetime.now()])
    db.modifydatabase(sqlcode, ['Zy Boco', datetime.now()])

    # Just some feedback that the code succeeded
    print('done!')


sql_query = """ SELECT * FROM owners"""
values = []
# number of column names must match the attributes for table genres
columns = ['id', 'name', 'contact', 'modified', 'is_deleted']

df = db.querydatafromdatabase(sql_query, values, columns)
print(df)

sql_resetowners = """
 TRUNCATE TABLE owners RESTART IDENTITY CASCADE
"""
db.modifydatabase(sql_resetowners, [])
addfewowners()
df = db.querydatafromdatabase(sql_query, values, columns)
print(df)
