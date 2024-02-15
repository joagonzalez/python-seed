"""
This module expose endpoints with main app features
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
