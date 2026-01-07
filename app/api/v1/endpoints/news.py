from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.crud.news import get_news_categories, get_news_count, get_news_list
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


@router.get("/list", summary="获取新闻列表")
async def get_news(
    category_id: int = Query(..., alias="categoryId", description="分类ID"),
    page: int = Query(1, description="页码"),
    page_size: int = Query(10, le=100, alias="pageSize", description="每页数量"),
    db: AsyncSession = Depends(get_db)   # 数据库会话依赖注入
    ):

    # 这里应调用CRUD层函数获取数据，示例中返回静态数据
    offset = (page - 1) * page_size
    news_list = await get_news_list(db, category_id, offset, page_size)
    total =  await get_news_count(db, category_id)
    has_more = (offset + len(news_list)) < total

    return {
        "code": 200,
        "message": "success",
        "data": {
            "list": news_list,
            "total": total,
            "hasMore": has_more
        }
    }