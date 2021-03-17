from april.connector import connect

database = connect()
global cursor 
cursor = database.cursor()

def generateId():
    database = connect()
    cursor = database.cursor()
    sql = "SELECT id FROM materials WHERE materialid = (SELECT MAX(id) FROM users)"
    cursor.execute(sql)
    try:
        id = cursor.fetchall()[0][0]
    except:
        id = 0
    return id + 1

def newMaterial(username, title, content):
    sql = "INSERT INTO materials VALUES ( %s, %s, %s, %s, %s )"
    now = datetime.now().strftime('%Y-%m-%d')
    vals = (generateId(), username, title, content, now)
    cursor.execute(sql, vals)
    database.commit()
