from fastapi import FastAPI

from app.config.db_config import Base, engine
from app.config.vars_config import settings
from app.routes import routes_mapper
from app.utils.constants import API_VERSION

app = FastAPI(
    title="Data Validation Framework",
    description="Validating the data at different zones by using FastAPI.",
    version="0.0.1",
    contact={"name": "Shaik Malik Basha", "email": "shaikmalikbasha@example.com"},
    license_info={"name": "MIT"},
)


@app.on_event("startup")
async def on_startup():
    print("Initializing the database")
    Base.metadata.create_all(bind=engine)
    print("Database was successfully created...")


@app.get("/", tags=["Default ROOT API"])
async def index():
    return {"msg": "Hello, World!", "appName": settings.APP_NAME}


app.include_router(routes_mapper.router, prefix=API_VERSION)
