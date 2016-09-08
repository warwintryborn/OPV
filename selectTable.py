import sqlite3

conn = sqlite3.connect('dbOPV.db')
cursor = conn.cursor()

# SELECT NA TABELA
cursor.execute("""
SELECT * FROM sensorWeb;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()
