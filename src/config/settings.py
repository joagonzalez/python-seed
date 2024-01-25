import os
from typing import Any, Dict

from dotenv import load_dotenv

dotenv_path = os.getenv(
    "API_DOTENV", os.path.join(os.path.dirname(__file__), ".env")
)

load_dotenv(dotenv_path, override=True)  # priorizes env vars (not .env file)

config: Dict[str, Any] = {
    "SERVER": {
        "HOSTNAME": os.getenv("SERVER_HOSTNAME", "0.0.0.0"),
        "PORT": int(os.getenv("SERVER_PORT", 5000)),
        "DEBUG": os.getenv("SERVER_DEBUG", "True").lower()
        in ("true", "1", "t"),
        "RELOAD": os.getenv("SERVER_RELOAD", "False").lower()
        in ("true", "1", "t"),
        "RELOAD_DIRS": [
            os.getenv("SERVER_RELOAD_DIRS", "src"),
        ],
        "LOG_LEVEL": os.getenv("SERVER_LOG_LEVEL", "debug"),
        "WORKERS": int(os.getenv("SERVER_WORKERS", 5)),
    },
    "API": {
        "ENVIRONMENT": os.getenv("API_ENVIRONMENT", "local"),
        "TITLE": os.getenv("API_TITLE", "Foundations-Networking Core API"),
        "DESCRIPTION": os.getenv(
            "API_DESCRIPTION",
            "REST interface that expose interactions with network elements",
        ),
        "VERSION": os.getenv("API_VERSION", ""),
        "USERNAME": os.getenv("API_USERNAME", ""),
        "PASSWORD": os.getenv("API_PASSWORD", ""),
    },
    "SWAGGER": {
        "DOCS_URL": os.getenv("SWAGGER_DOCS_URL", "/docs"),
        "REDOC_URL": os.getenv("SWAGGER_REDOC_URL", "/redoc_docs"),
    },
    "JWT": {
        "SECRET_KEY": os.getenv("JWT_SECRET_KEY", ""),
        "ALGORITHM": os.getenv("JWT_ALGORITHM", ""),
        "ACCESS_TOKEN_EXPIRE_MINUTES": int(
            os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30)
        ),
    },
    "DATABASE": {
        "SQLALCHEMY": {
            "PREFIX": os.getenv("SQLALCHEMY_DATABASE_PREFIX", "DB."),
            "CONFIG": {
                "DB.URL": os.getenv("SQLALCHEMY_DATABASE_URL", ""),
                "DB.ECHO": bool(os.getenv("SQLALCHEMY_DATABASE_ECHO", True)),
            },
        },
    },
}

PROMPT = """
     ___      .______    __          _______. _______  _______  _______  
    /   \     |   _  \  |  |        /       ||   ____||   ____||       \
   /  ^  \    |  |_)  | |  |       |   (----`|  |__   |  |__   |  .--.  |
  /  /_\  \   |   ___/  |  |        \   \    |   __|  |   __|  |  |  |  |
 /  _____  \  |  |      |  |    .----)   |   |  |____ |  |____ |  '--'  |
/__/     \__\ | _|      |__|    |_______/    |_______||_______||_______/

"""  # noqa: W605, E261, W291