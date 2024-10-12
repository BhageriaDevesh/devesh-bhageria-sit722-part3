from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Use the Render PostgreSQL URL directly
SQLALCHEMY_DATABASE_URL = "postgresql://hanuman_user:a4OxAtL6qUk8eXUdPqWw4S0RfVhGc8t7@35.227.164.209/hanuman"

# Create the engine to connect to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()