from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String)
    owner_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Property(name={self.name}, address={self.address}, price={self.price})>"