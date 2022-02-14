import sqlite3

con = sqlite3.connect('emails.db')

cur = con.cursor()

# Create table
cur.execute(
    '''CREATE TABLE IF NOT EXISTS emails
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name varchar(50), 
        phone varchar(25),
        email varchar(50));''')

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()