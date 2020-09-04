from fastapi import FastAPI

from modules.core import api_heath_check
from modules.posts.routers import router as posts_routers

from modules.posts import models
from db import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)


app.include_router(api_heath_check.router)
app.include_router(posts_routers, prefix="/posts", tags=["posts"])
