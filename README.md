# Agent Development Kit

## Overview

Simple ADK application, based on: [www.jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/).

It leverages:

- **ADK (Agent Development Kit)** for agent development
- **A2A (Agent-to-Agent)** protocol for inter-agent communication

## Architecture Layers

### 1. Agent Layer (A2A Communication)

- **Supervisor Agent**: Orchestrates workflow, coordinates sub-agents, handles routing and error handling
- **Users Agent**: Receive and format data
- **Posts Agent**: Receive and format data
- **Comments Agent**: Receive and format data

### 2. AI Platform

- Vertex AI (LLM, Gemini) for reasoning and NLP

## Folder Structure

```
ADKs/
│
├── infrastructure/
│   │
│   └── docker/
│       └── docker-compose.yml
│
├── agents/
│   │
│   ├── supervisor/
│   │   │
│   │   ├── src/
│   │   │   │
│   │   │   └── instructions/
│   │   │       ├── instructions.md
│   │   │       └── instructions_loader.py
│   │   │
│   │   ├── .env.example.py
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   └── agent.py
│   │
│   ├── posts/
│   │   │
│   │   ├── src/
│   │   │   │
│   │   │   ├── instructions/
│   │   │   │   ├── instructions.md
│   │   │   │   └── instructions_loader.py
│   │   │   │
│   │   │   ├── clients/
│   │   │   │   └── posts_client.py
│   │   │   │
│   │   │   ├── pipelines/
│   │   │   │   └── posts_pipeline.py
│   │   │   │
│   │   │   └── tools/
│   │   │       ├── formatters.py
│   │   │       └── posts_service.py
│   │   │
│   │   ├── .env.example.py
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   └── agent.py
│   │   
│   ├── users/
│   │   │
│   │   ├── src/
│   │   │   │
│   │   │   ├── instructions/
│   │   │   │   ├── instructions.md
│   │   │   │   └── instructions_loader.py
│   │   │   │
│   │   │   ├── clients/
│   │   │   │   └── users_client.py
│   │   │   │
│   │   │   ├── pipelines/
│   │   │   │   └── users_pipeline.py
│   │   │   │
│   │   │   └── tools/
│   │   │       ├── formatters.py
│   │   │       └── users_service.py
│   │   │
│   │   ├── .env.example.py
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   └── agent.py
│   │
│   └── comments/
│       │
│       ├── src/
│       │   │
│       │   ├── instructions/
│       │   │   ├── instructions.md
│       │   │   └── instructions_loader.py
│       │   │
│       │   ├── clients/
│       │   │   └── comments_client.py
│       │   │
│       │   ├── pipelines/
│       │   │   └── comments_pipeline.py
│       │   │
│       │   └── tools/
│       │       ├── formatters.py
│       │       └── comments_service.py
│       │
│       ├── .env.example.py
│       ├── main.py
│       ├── requirements.txt
│       ├── Dockerfile
│       └── agent.py
│
├── .gitignore
├── deps_install.py
├── LICENSE
└── README.md
```

## Deployment Architecture

Each agent is deployed as an independent Cloud Run service:

### Agents (Cloud Run Services)

- `supervisor-agent`
- `users-agent`
- `posts-agent`
- `comments-agent`

## Technology Stack

- **Agent Framework**: ADK (Agent Development Kit)
- **Agent Communication**: A2A Protocol
- **Cloud Platform**: Google Cloud Platform
- **Deployment**: Cloud Run (serverless containers)
- **AI/ML**: Vertex AI (Gemini)
- **Language**: Python 3.11+

## Communication Flow

1. **Supervisor Flow**: JSONPlaceholder → Sub Agent → Supervisor Agent → User
2. **Users Flow**: JSONPlaceholder → Users Agent → Response Formatter → Supervisor Agent
3. **Posts Flow**: JSONPlaceholder → Posts Agent → Response Formatter → Supervisor Agent
4. **Comments Flow**: JSONPlaceholder → Comments Agent → Response Formatter → Supervisor Agent

## Getting Started

### Prerequisites

- Python 3.11+
- Docker
- Google Cloud SDK

### Local development:

1. create venv: `py -m venv .venv` in **root** directory
2. activate env:
    - **macOS/Linux:** `source .venv/bin/activate`
    - **CMD:**`.venv\Scripts\activate.bat`
    - **PowerShell:**`.venv\Scripts\Activate.ps1`
3. pass own credentials file in .env: **check** `.env.example` into agents directories
4. install packages: `py .\deps_install.py`
5. run: `adk web` from **/agents** directory
6. open: [127.0.0.1:8000](http://127.0.0.1:8000)

### Docker:

1. go to `infrastructure/docker/`
2. build: `docker coompose build`
3. up: `docker compose up`
4. build & up: `docker compose up --build`
4. open: [127.0.0.1:8000](http://127.0.0.1:8000)

## License

MIT License.