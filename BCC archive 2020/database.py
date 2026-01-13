import MySQLdb
# install pip (package) from python to get MySQLdb

db = MySQLdb.connect(host='host',
                     user='user',
                     passwd='password',
                     db='name')
# set variables for database to read the proper info

cur = db.cursor()

cur.execute('SELECT * FROM top5')
# selecting table from the database

for row in cur.fetchall():
    print(row)

db.close()
#closes after database gets info

# from MySQLdb import connect

# DB_HOST = 'host'  # IP or hostname of database
# DB_NAME = 'name'  # Name of the database to use
# DB_USER = 'user'  # Username for accessing database
# DB_PASS = 'password'  # Password for database user

# db_connection = connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)
