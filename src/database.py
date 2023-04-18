import sqlite3

database = "database.db"

def createDatabase():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    msgTable = """CREATE TABLE IF NOT EXISTS messages(
        message_id INTEGER PRIMARY KEY, 
        sender TEXT, 
        reciever TEXT,
        message BLOB);"""
    cursor.execute(msgTable)

    cursor.commit()
    cursor.close()

def sendMessage(sender, reciever, message):
    connection = sqlite3.connect(database)
    cursor = connection.cursor

    sendMsg = """INSERT INTO messages(sender, reciever, message) VALUES (?, ?, ?)"""
    cursor.execute(sendMsg, (sender, reciever, message))

    cursor.commit()
    cursor.close()
