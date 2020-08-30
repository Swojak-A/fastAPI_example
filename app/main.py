from fastapi import Depends, FastAPI, Header, HTTPException

from modules.core import api_heath_check

app = FastAPI()


app.include_router(api_heath_check.router)
