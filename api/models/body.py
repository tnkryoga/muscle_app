from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from api.db import Base


class Body(Base):
    __tablename__ = "bodys"
    id = Column(Integer,primary_key=True)
    muscle_mass = Column(Float,nullable=False)
    weight = Column(Float,nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"),nullable=False)
