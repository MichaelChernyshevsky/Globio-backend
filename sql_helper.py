import sqlite3
# constants 
from constants.sql_constants import SQLConstants


def insertDataIntoTable(table,request,data,tableName):
    conn = sqlite3.connect(table)
    cursor = conn.cursor()  
    cursor.execute(request)
    for name, age in data:
        cursor.execute(f"INSERT INTO {tableName}(name, age) VALUES (?, ?)", (name, age))
    # Сохранение изменений
    conn.commit()
    # Закрытие соединения
    conn.close()

def getDataFromTable(table,request):
    conn = sqlite3.connect(table)
    cursor = conn.cursor()
    cursor.execute(request)
    rows = cursor.fetchall()
    conn.close()
    return rows


insertDataIntoTable(
    table=SQLConstants.user_table_file,
    request=SQLConstants.getTable(SQLConstants.user_table_name),
    data=[("Иван Петров", 25), ("Мария Иванова", 30)],
    tableName = SQLConstants.user_table_name,)
getDataFromTable(table=SQLConstants.user_table_file,request=SQLConstants.getAllRequest(SQLConstants.user_table_name))

