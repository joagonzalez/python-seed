"""
API Health endpoints used to monitor the application
from external tools and applications
"""

from typing import Dict

from fastapi import APIRouter

router = APIRouter()


@router.get("/status/", tags=["Health"])
async def get_health() -> Dict[str, str]:
    """Returns a dictionary with internal app status

    Returns:
        Dict[str, str]: single key dict with status message
    """
    return {"status": "OK"}
