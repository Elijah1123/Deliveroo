from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt


import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_URI') 
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
# SQLALCHEMY_URI and SECRET_KEY should be set in the .env file
