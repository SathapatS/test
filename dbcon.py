import pyodbc

password = 'cal'

try:
    conn_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Lenovo\Desktop\Coding\Flask\pjk1\Lab.accdb;PWD='+ password
    conn = pyodbc.connect(conn_string)
    print("connected to database")
except pyodbc.Error as e :
    print("Error connection", e)
