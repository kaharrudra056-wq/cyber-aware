import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cybersec-dev-secret-2024'

    # External PostgreSQL or local SQLite
    DATABASE_URL = os.environ.get('DATABASE_URL')

    if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
        # Fix for newer SQLAlchemy requiring postgresql://
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

    SQLALCHEMY_DATABASE_URI = DATABASE_URL or 'sqlite:///cybersecurity.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
