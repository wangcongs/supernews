from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.config import settings


# 从配置中获取数据库连接字符串
DATABASE_URL = settings.DATABASE_URL

# SQLAlchemy 异步引擎配置
async_engine = create_async_engine(
    DATABASE_URL, # 输出日志
    echo=True,  # 启用连接池
    future=True, # 使用 SQLAlchemy 2.0 风格
    pool_pre_ping=True, # 检测连接有效性
    pool_size=10, # 连接池大小
    max_overflow=20 # 连接池溢出大小
    )

# 创建异步会话工厂
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine, # 绑定异步引擎
    class_=AsyncSession, # 使用异步会话类
    expire_on_commit=False, # 提交后不失效对象
    future=True # 使用 SQLAlchemy 2.0 风格
)

# 依赖注入：获取异步数据库会话
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
# 供外部导入使用
__all__ = ["async_engine", "AsyncSessionLocal", "get_db"]  


