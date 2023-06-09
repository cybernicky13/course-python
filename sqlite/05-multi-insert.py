import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Guts"),
        (3, "Griffith"),
    ]
    cursor.executemany(
        "insert into usuarios values(?,?)",
        usuarios,    
    )