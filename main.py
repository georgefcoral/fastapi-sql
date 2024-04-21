from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.restaurant import restaurant_router

app = FastAPI()
app.title = "Restaurant API"
app.version = "0.0.1"
app.description = "API for restaurant manager"

app.add_middleware(ErrorHandler)

app.include_router(restaurant_router)

Base.metadata.create_all(bind=engine)


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')
