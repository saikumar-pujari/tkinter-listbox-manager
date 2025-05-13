import sqlite3
##in place of memory u can write your database name but it will create a new file in your system as the name db of your file
##in memory it doesnot create any file 
conn=sqlite3.connect(":memory:")
##cursor is a genral utility function
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS books(title TEXT,pages INTEGER)')
# c.execute('INSERT INTO books VALUES("SAIKUMAR",32)')
# c.execute('INSERT INTO books VALUES("SAINATH",45)')
#conn.commit()
books=[
    ('saikuamr',54),
    ('nikihil',5465),
    ('sainath',6545)
]
###create
c.executemany('INSERT INTO books VALUES(?,?)',books)
conn.commit()

##read
c.execute('SELECT rowid,title FROM books')
# c.execute('SELECT *FROM books where title="sainath"')
data=c.fetchall()
print(data)


##update
c.execute("UPDATE books SET title='saikumar' where rowid=1")
c.execute('SELECT rowid,title FROM books')
data=c.fetchall()
print(data)

##DELETE
c.execute('DELETE FROM books where rowid=2')
conn.commit()
c.execute('SELECT *FROM books')
data=c.fetchall()
print(data)
conn.close()