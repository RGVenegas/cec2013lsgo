import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('C:/Users/rorov/PycharmProjects/taller-2-entrega-2/bd_ddyaadaa.db')
cursor = conn.cursor()

# Ejecutar script SQL para crear la tabla
with open('bd_ddyaadaa.sql', 'r') as file:
    create_table_query = file.read()
    cursor.executescript(create_table_query)

# Listar las tablas en la base de datos
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tablas en la base de datos:", tables)

conn.close()
