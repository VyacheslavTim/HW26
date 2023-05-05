import os


class Config:
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST')
    # SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_password@localhost:5436/db_name'
