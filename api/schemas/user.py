from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    done: bool = Field(False, description="完了フラグ")
    
class UserCreate(UserBase):
    pass

class UserCreateResponse(UserCreate):
    pass

class User(UserBase):
    pass