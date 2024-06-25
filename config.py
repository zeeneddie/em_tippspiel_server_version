from flask import Flask
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import os

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["DEBUG"] = True
Session(app)

# Configure SQLAlchemy for MySQL database
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}'.format(
    username = os.getenv('DB_USERNAME'),
    password = os.getenv('DB_PASSWORD'),
    hostname = os.getenv('DB_HOSTNAME'),
    databasename = os.getenv('DB_DATABASE')
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create SQLAlchemy engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session_db = Session()