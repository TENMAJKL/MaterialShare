#soubor na vytvoreni material objektu, pouze GET

from april.connector import connect


database = connect()
global cursor 
cursor = database.cursor()

def getBySearch(searchTerm):
    sql = "SELECT * FROM materials WHERE content LIKE CONCAT('%', %s, '%')"
    cursor.execute(sql, (searchTerm,))
    return cursor.fetchall()

  
def getById(id):
    sql = "SELECT * FROM materials WHERE id = %s"
    vals = (id)
    cursor.execute(sql, vals)
    return cursor.fetchall()

def getByUser(userName):
    sql = "SELECT * FROM materials WHERE userName = %s"
    vals = (userName)
    cursor.execute(sql, vals)
    return cursor.fetchall()

def getSaved(userID):
    sql = "SELECT id FROM savedMaterials WHERE userId = %s"
    vals = (userID)
    cursor.execute(sql, vals)
    return cursor.fetchall()



