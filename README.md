# Agent Development Kit

## Overview

Simple ADK application, which works with: [www.jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/)

## Folder Structure

```
ADKs/
├── infrastructure/
│   └── docker/
│       └── docker-compose.yml
├── jsonplaceholder_adk/
│   ├── agents/
│   │   ├── posts/
│   │   │   ├── instructions/
│   │   │   │   ├── __init__.py
│   │   │   │   └── posts.py
│   │   │   ├── schemas/
│   │   │   │   ├── __init__.py
│   │   │   │   └── posts.py
│   │   │   ├── tools/
│   │   │   │   ├── __init__.py
│   │   │   │   └── jsonplaceholder_posts.py
│   │   │   ├── __init__.py
│   │   │   ├── post_pipeline.py
│   │   │   └── posts_pipeline.py
│   │   ├── users/
│   │   │   ├── instructions/
│   │   │   │   ├── __init__.py
│   │   │   │   └── users.py
│   │   │   ├── schemas/
│   │   │   │   ├── __init__.py
│   │   │   │   └── users.py
│   │   │   ├── tools/
│   │   │   │   ├── __init__.py
│   │   │   │   └── jsonplaceholder_users.py
│   │   │   ├── __init__.py
│   │   │   ├── user_pipeline.py
│   │   │   └── users_pipeline.py
│   │   ├── comments/
│   │   │   ├── instructions/
│   │   │   │   ├── __init__.py
│   │   │   │   └── comments.py
│   │   │   ├── schemas/
│   │   │   │   ├── __init__.py
│   │   │   │   └── comments.py
│   │   │   ├── tools/
│   │   │   │   ├── __init__.py
│   │   │   │   └── jsonplaceholder_comments.py
│   │   │   ├── __init__.py
│   │   │   ├── comment_pipeline.py
│   │   │   └── comments_pipeline.py
│   │   ├── __init__.py
│   │   └── root.py
│   ├── shared/
│   │   ├── callbacks/
│   │   │   ├── __init__.py
│   │   │   └── formatting.py
│   │   ├── clients/
│   │   │   ├── __init__.py
│   │   │   └── jsonplaceholder_client.py
│   │   ├── constants/
│   │   │   ├── __init__.py
│   │   │   ├── formatting.py
│   │   │   └── pipelines.py
│   │   └── __init__.py
│   ├── agent.py
│   ├── Dockerfile
│   └── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

## Technology Stack

- **Agent Framework**: ADK (Agent Development Kit)
- **Cloud Platform**: Google Cloud Platform
- **Deployment**: Cloud Run (serverless containers)
- **AI/ML**: Vertex AI (Gemini)
- **Language**: Python 3.11+

### Agents

- `jsonplaceholder_adk`

## Getting Started

### Prerequisites

- Python 3.11+
- Docker
- Google Cloud SDK

### Local development:

1. create venv: `py -m venv .venv`
2. pass own credentials file in .env: **check** `.env.example`
3. activate env:
    - **macOS/Linux:** `source .venv/bin/activate`
    - **CMD:**`.venv\Scripts\activate.bat`
    - **PowerShell:**`.venv\Scripts\Activate.ps1`
4. packages:
    - **Bash:** `python -m pip install -r requirements.txt`
    - **PowerShell:** `py -m pip install -r requirements.txt`
5. run: `adk web`
6. open: [127.0.0.1:8000](http://127.0.0.1:8000)

### Docker:

1. build: `docker compose --env-file .env -f infrastructure/docker/docker-compose.yml build`
2. run: `docker compose --env-file .env -f infrastructure/docker/docker-compose.yml up`
3. build & run: `docker compose --env-file .env -f infrastructure/docker/docker-compose.yml up --build`
4. open: [127.0.0.1:8000](http://127.0.0.1:8000)

## License

MIT License.