from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # Define the declarative base class


class State(Base):
    """
    State class representing the states table in a MySQL database.
    """

    __tablename__ = 'states'  # Table name

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


# This line should be placed elsewhere where engine is created
# Base.metadata.create_all(engine)

