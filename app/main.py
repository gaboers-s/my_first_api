from fastapi import FastAPI
from app.routes import quote_routes
app = FastAPI(
    title = "a quote api",
    description = "api for quotes",
    version = "1.0.0"
)

app.include_router(quote_routes.router)