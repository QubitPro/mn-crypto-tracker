"""FastAPI application entry point."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Real-time crypto portfolio tracker",
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "version": settings.VERSION}