from fastapi import APIRouter

router = APIRouter()


@router.get("/check")
async def api_health_check():
    return {"status": "ok"}
