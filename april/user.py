#soubor na vytvoreni user objektu


from april.connector import connect


class getUser:

  def __init__(self, name):
    self.name = name

    database = connect()
    cursor = database.cursor()
    sql = "SELECT * FROM users WHERE name = %s"
    vals = (self.name,)
    cursor.execute(sql, vals)
    global userInfo 
    userInfo = cursor.fetchall()[0]


  def getId(self):
    return userInfo[0]
  
  def getName(self):
    return userInfo[1]

  def getPassword(self):
    return userInfo[2]

  def getPhoto(self):
    return userInfo[3]
  
  def getDescription(self):
    return userInfo[4]

