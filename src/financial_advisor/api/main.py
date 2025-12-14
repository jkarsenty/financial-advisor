"""
Main entrypoint for the FastAPI backend.

This module initializes the FastAPI application, configures global settings,
and registers all API routes.

TODO:
- Add CORS configuration if needed (Step 2 when frontend arrives)
- Add versioning or prefix if required (e.g., /api/v1)
- Add logging middleware (Step 3)
"""

from fastapi import FastAPI

from financial_advisor.api.routes.incomes import router as incomes_router
from financial_advisor.api.routes.expenses import router as expenses_router
from financial_advisor.api.routes.summary import router as summary_router


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: The configured FastAPI instance.
    """
    app = FastAPI(
        title="Financial Advisor API",
        description="Backend API exposing financial calculations, summaries and utilities.",
        version="0.1.0",
    )

    # Register routers
    app.include_router(incomes_router, prefix="/api")
    app.include_router(expenses_router, prefix="/api")
    app.include_router(summary_router, prefix="/api")

    @app.get("/health", tags=["system"])
    def health_check() -> dict:
        """Simple health check endpoint."""
        return {"status": "ok"}

    return app


# FastAPI convention:
# The "app" variable is what uvicorn loads.
app = create_app()
