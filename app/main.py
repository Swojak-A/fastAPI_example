from fastapi import FastAPI

from modules.core import api_heath_check
from modules.posts.routers import router as posts_routers
from modules.comments.routers import router as comments_router

import all_models
from db import engine

modules = ["modules.posts.models"]

all_models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)


app.include_router(api_heath_check.router)
app.include_router(posts_routers, prefix="/posts", tags=["posts"])
app.include_router(comments_router, prefix="/comments", tags=["comments"])
