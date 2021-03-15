#soubor na vytvoreni user objektu


from april.connector import connect
from datetime import datetime


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
    return userInfo[6]
  
  def getDescription(self):
    return userInfo[4]
  
  def getMail(self):
    return userInfo[3]

  def getDbPerm(self):
    return userInfo[7]

def mailInDb(mail):
  database = connect()
  cursor = database.cursor()
  sql = "SELECT * FROM users WHERE email = %s"
  vals = (mail,)
  cursor.execute(sql, vals)
  users = cursor.fetchall()
  try:
    users[0]
    isin = True
  except:
    isin = False
  return isin

def nameInDb(name):
  database = connect()
  cursor = database.cursor()
  sql = "SELECT * FROM users WHERE name = %s"
  vals = (name,)
  cursor.execute(sql, vals)
  users = cursor.fetchall()
  try:
    users[0]
    isin = True
  except:
    isin = False
  return isin

def generateId():
  database = connect()
  cursor = database.cursor()
  sql = "SELECT id FROM users WHERE id = (SELECT MAX(id) FROM users)"
  cursor.execute(sql)
  try:
    id = cursor.fetchall()[0][0]
  except:
    id = 0
  return id + 1

def register(name, password, mail):
  database = connect()
  cursor = database.cursor()
  sql = "INSERT INTO users (id,	name,	password, email, profiledate) VALUES(%s, %s, %s, %s, %s)"
  now = datetime.now().strftime('%Y-%m-%d')
  id = str(generateId())
  vals = (id, name, password, mail, now, )
  print(vals)
  cursor.execute(sql, vals)
  database.commit()