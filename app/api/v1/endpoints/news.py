from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.crud.news import get_news_categories
from app.db.session import get_db


# 创建news路由器
router = APIRouter()

# 定义获取新闻分类的GET接口
@router.get("/categories", summary="获取新闻分类")
async def get_categories(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    # 这里应调用CRUD层函数获取数据，示例中返回静态数据
    categories = await get_news_categories(db, skip, limit)

    return {
        "code": 200,
        "message": "success",
        "data": categories
    }