from typing import List, Optional

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.skill import Skill

class SkillService:
    @staticmethod
    async def get_all(session: AsyncSession):
        result = await session.execute(select(Skill))
        return result.scalars().all()

    @staticmethod
    async def get_by_id(session:AsyncSession, skill_id: int):
        result = await session.execute(select(Skill).filter(Skill.id == skill_id))
        return result.scalars().first()

    @staticmethod
    async def create(session:AsyncSession, name: str, description: str, user_id: int):
        new_skill = Skill(name = name,description = description,user_id = user_id)
        session.add(new_skill)
        await session.commit()
        await session.refresh(new_skill)
        return new_skill

    @staticmethod
    async def delete(session: AsyncSession,skill_id: int):
        skill = await SkillService.get_by_id(session,skill_id)
        if not skill:
            return
        await session.delete(skill)
        await session.commit()