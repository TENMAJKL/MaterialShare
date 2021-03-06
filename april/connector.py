#connector pro databazi

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def connect():
  database = mysql.connector.connect(
    host=os.getenv("DBHOST"),
    user=os.getenv("DBUSER"),
    password=os.getenv("DBPASSWORD"),
    database=os.getenv("DBNAME")
    )
  return database
