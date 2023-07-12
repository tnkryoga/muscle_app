from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from api.db import Base


class Nutrition(Base):
    __tablename__ = "nutritions"
    id = Column(Integer,primary_key=True)
    nutritious = Column(String(100),nullable=False)
    quantity = Column(Float,nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"),nullable=False)
