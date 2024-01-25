from typing import Dict

from fastapi import APIRouter, Security

router = APIRouter()


@router.get("/status/", tags=["Health"])
async def get_health() -> Dict[str, str]:
    return {"status": "OK"}
