from fastapi import FastAPI

from app.config.db_config import Base, engine
from app.routes import routes_mapper
from app.utils.constants import API_VERSION

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    print("Initializing the database")
    Base.metadata.create_all(bind=engine)
    print("Database was successfully created...")


@app.get("/")
async def index():
    return {"msg": "Hello, World!"}


app.include_router(routes_mapper.router, prefix=API_VERSION)
