import sqlite3

database = "database.db"

def createDatabase():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    command = """CREATE TABLE IF NOT EXISTS messages(
        message_id INTEGER PRIMARY KEY, 
        sender TEXT, 
        reciever TEXT,
        message BLOB);"""
    cursor.execute(command)

    connection.commit()
    connection.close()

def addMessage(sender, reciever, message):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    command = "INSERT INTO messages (sender, reciever, message) VALUES (?, ?, ?)"
    cursor.execute(command, (sender, reciever, message))

    connection.commit()
    connection.close()
