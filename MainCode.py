import mysql.connector
UTTSdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='harsh',
    database='UTTS')
#print(UTTSdb.connection_id)
#print to check connection establishment
cur=UTTSdb.cursor()
s="SELECT * from users"
cur.execute(s)
result=cur.fetchall()

print(result)