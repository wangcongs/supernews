from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from typing import AsyncGenerator
from contextlib import asynccontextmanager
import logging

from app.core.config import settings
from app.api.v1.routers import api_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
	"""应用生命周期管理器（lifespan）。

	在这里运行启动与关闭任务：
	- 启动时初始化数据库（可扩展为连接消息队列、缓存等）
	- 关闭时进行清理

	采用 asynccontextmanager 以兼容 FastAPI 新版本中弃用的 `@app.on_event` 方式。
	"""
	logger.info("应用启动：初始化资源")
	# 在此处执行数据库初始化或迁移等一次性启动操作
	# init_db()
	try:
		yield
	finally:
		# 可在此处关闭连接、flush 日志或其他清理操作
		logger.info("应用关闭：清理资源")


def create_app() -> FastAPI:
	"""创建并返回 FastAPI 应用实例。

	- 使用 `lifespan` 管理启动/关闭任务
	- 注册基础中间件（例如 CORS）
	- 挂载 API 路由器
	"""
	app = FastAPI(
		title=settings.PROJECT_NAME,
		version=settings.VERSION,
		lifespan=lifespan,
		docs_url="/docs",
		redoc_url="/redoc",
		openapi_url="/openapi.json",
	)

	# 开发时允许全部跨域（生产环境请改为具体域名白名单）
	app.add_middleware(
		CORSMiddleware,
		allow_origins=["*"],
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)

	# 挂载版本化 API 路由
	app.include_router(api_router)

	
	return app


# 导出应用实例，uvicorn 可直接通过 `app` 启动
app = create_app()

