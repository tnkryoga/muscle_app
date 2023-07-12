from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    password = Column(String(20), nullable=False)
    mail = Column(String(100), nullable=False)
    name = Column(String(40), nullable=False)
    age = Column(Integer, nullable=False)
    create_at = Column(Integer, nullable=False)
