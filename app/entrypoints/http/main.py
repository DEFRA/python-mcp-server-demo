from contextlib import AsyncExitStack, asynccontextmanager
from logging import getLogger

import uvicorn
from fastapi import FastAPI

from app.common.mongo import get_mongo_client
from app.common.tracing import TraceIdMiddleware
from app.config import config
from app.health.router import router as health_router
from app.mcp.demo_server.server import demo_mcp_server

logger = getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Startup
    client = await get_mongo_client()
    logger.info("MongoDB client connected")

    async with AsyncExitStack() as stack:
        await stack.enter_async_context(demo_mcp_server.session_manager.run())
        yield

    # Shutdown
    if client:
        await client.close()
        logger.info("MongoDB client closed")

api = FastAPI(lifespan=lifespan)

# Setup middleware
api.add_middleware(TraceIdMiddleware)

# Setup Routes
api.include_router(health_router)

api.mount("/", demo_mcp_server.streamable_http_app())


def main() -> None:
    uvicorn.run(
        "app.entrypoints.http.main:api",
        host=config.host,
        port=config.port,
        log_config=config.log_config,
        reload=config.python_env == "development"
    )


if __name__ == "__main__":
    main()
