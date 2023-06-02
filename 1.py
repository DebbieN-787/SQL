import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='Wolf-e-777')
cursor = conn.cursor()
cursor.close()
conn.close()