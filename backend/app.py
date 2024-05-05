from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient, errors
import os
import sys

#Load .env variables
load_dotenv()

MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")

uri = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@mydb.mvvqibf.mongodb.net/?retryWrites=true&w=majority&appName=MyDB"

try:
  client = MongoClient(uri)
except errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

db = client.URLS
collection = db["urlsTesting"]

app = Flask(__name__)

@app.route("/")
def greeting():
  return "Hola mamada"

# @app.route("/short", methods=["POST"])
# def short_url:

# @app.route("/:urlID", methods=["GET"])
# def redirect:
