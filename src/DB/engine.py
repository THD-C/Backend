import os
from sqlmodel import create_engine
from sqlalchemy import create_engine

LOCALHOST_PG = "postgresql://default:PL_tech_hand_elk@localhost:5432/verceldb"

connection_string = os.getenv("POSTGRES_URL", LOCALHOST_PG).replace("postgres://","postgresql://")

engine = create_engine(connection_string)
