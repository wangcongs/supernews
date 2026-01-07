from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.news import Category


async def get_news_categories(db: AsyncSession, skip: int = 0, limit: int = 100):
    """获取新闻分类的示例接口"""
    stmt = select(Category).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()