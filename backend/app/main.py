from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine, Base
from app.api import tasks, webhooks


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Board API",
    description="B2B Task Board App",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Temporary: allow all for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoints
@app.get("/")
async def root():
    return {"message": "Task Board API is running"}

@app.get("/health")
async def health():
    return {"status": "ok"}

app.include_router(tasks.router)
app.include_router(webhooks.router)