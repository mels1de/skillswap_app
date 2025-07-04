from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.skill import SkillCreate, SkillOut
from app.services.skill_service import SkillService
from app.db.database import get_async_session
from app.api.auth import get_current_user
from app.models.user import User

router = APIRouter(tags=["skills"],prefix="/skills")

@router.get("/",response_model=List[SkillOut])
async def read_skills(session: AsyncSession = Depends(get_async_session)):
    return await SkillService.get_all(session)

@router.get("/{skill_id}",response_model=SkillOut)
async def read_skill(skill_id: int, session: AsyncSession = Depends(get_async_session)):
    skill = await SkillService.get_by_id(session,skill_id)
    if not skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="skill not found")
    return skill
@router.post(
    "/",
    response_model=SkillOut,
    status_code=status.HTTP_201_CREATED
)
async def create_skill(
        payload: SkillCreate,
        current_user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_async_session)
):
    return await SkillService.create(
        session,
        name=payload.name,
        description=payload.description,
        user_id=current_user.id
    )

@router.delete("/{skill_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_skill(
    skill_id: int,
    current_user: User = Depends(get_current_user),
    session:AsyncSession = Depends(get_async_session)
):
    skill = await SkillService.get_by_id(session, skill_id)
    if not skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="skill not found")
    if skill.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not allowed!")
    await SkillService.delete(session, skill_id)