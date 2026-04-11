import os
import logging

SUPERVISOR_USE_A2A = os.environ.get("SUPERVISOR_USE_A2A", "false").lower() == "true"

if SUPERVISOR_USE_A2A:
    # A2A mode

    from agent import a2a_app as app

else:
    # FastAPI mode

    from fastapi import FastAPI
    from google.adk.cli.fast_api import get_fast_api_app

    AGENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SESSION_SERVICE_URI = "memory://"  # agent dialogs store (can be moved to settings.py file)
    ALLOWED_ORIGINS = ["*"]
    SERVE_WEB_INTERFACE = True

    app: FastAPI = get_fast_api_app(
        agents_dir=AGENT_DIR,
        session_service_uri=SESSION_SERVICE_URI,
        allow_origins=ALLOWED_ORIGINS,
        web=SERVE_WEB_INTERFACE,
        trace_to_cloud=False,
    )

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    logger = logging.getLogger(__name__)
    logger.info(f"Starting Supervisor Agent on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
