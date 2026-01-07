# News Platform (FastAPI + Vue)

企业级新闻网站模板，前后端分离：FastAPI 后端 + Vue 3 前端 (Vite + TypeScript)。

快速开始：

后端：（项目根）
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

前端：
```bash
cd frontend
pnpm install
pnpm dev
```

容器：
```bash
docker-compose up --build
```
