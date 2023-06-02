import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='Wolf-e-777')
cursor = conn.cursor()
cursor.execute('CREATE DATABASE menagerie')
table = cursor.fetchall()
conn.commit()
cursor.close()
conn.close()