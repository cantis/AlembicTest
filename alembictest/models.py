from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True)
    name = Column(Text, server_default = 'Sparkey')
    breed = Column(Text, nullable=False)

if __name__ == '__main__':
    d1, d2 = Dog(), Dog()

    sesh = sessionmaker(bind=create_engine('sqlite:///pets.db'))

    with sesh() as s:
        s.add_all([d1, d2])
        s.commit()