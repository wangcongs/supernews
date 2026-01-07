from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.news import Category, News


async def get_news_categories(db: AsyncSession, skip: int = 0, limit: int = 100):
    """获取新闻分类的示例接口"""
    stmt = select(Category).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()

async def get_news_list(db: AsyncSession, category_id: int, skip: int, limit: int):
    """获取新闻列表的示例接口"""
    stmt = select(News).where(News.category_id == category_id).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_news_count(db: AsyncSession, category_id: int) -> int:
    """获取指定分类的新闻总数"""
    stmt = select(func.count(News.id)).where(News.category_id == category_id)
    result = await db.execute(stmt)
    return result.scalar_one() # 只能有一个结果，返回多个就报错