from april.connector import connect
import mysql.connector

def loadCommand(command):
    db = connect()
    cursor = db.cursor()
    try:
        cursor.execute(command)
        try:
            return cursor.fetchall()
        except:
            db.commit()
            return [[f"Tabulka pozměněna; řádky: {cursor.rowcount}"]]
    except:
        return [["Nevim cos delal, ale posralsto"]]
        