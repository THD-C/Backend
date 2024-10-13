import os
from sqlmodel import create_engine
from sqlalchemy import create_engine


IP = os.getenv("DB_IP","localhost")
PORT = os.getenv('DB_Port', '5432')
DB_NAME = os.getenv('DB_Name', 'THD')


USERNAME = os.getenv('DB_User', 'THD')
PASSWORD = os.getenv('DB_Pass', 'PL_tech_hand_elk')

connection_string = f"postgresql://{USERNAME}:{PASSWORD}@{IP}:{PORT}/{DB_NAME}"
engine = create_engine(connection_string)