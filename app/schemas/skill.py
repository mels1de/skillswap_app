from pydantic import BaseModel
from typing import Optional

class SkillBase(BaseModel):
    name: str
    description: Optional[str] = None

class SkillCreate(SkillBase):
    user_id: int

class SkillOut(SkillBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True