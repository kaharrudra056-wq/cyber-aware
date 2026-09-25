import os
from dotenv import load_dotenv

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(ROOT_DIR, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cybersec-dev-secret-2024'

    DATABASE_URL = os.environ.get('DATABASE_URL') or ''

    if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

    DB_PATH = os.path.join(ROOT_DIR, 'database', 'cybersecurity.db')
    SQLALCHEMY_DATABASE_URI = DATABASE_URL if DATABASE_URL else f'sqlite:///{DB_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
