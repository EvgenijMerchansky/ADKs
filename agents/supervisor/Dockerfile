FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV SUPERVISOR_USE_A2A=false

WORKDIR /app

COPY agents/supervisor/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY agents/supervisor/ /app/supervisor/

ENV PYTHONPATH=/app

WORKDIR /app/supervisor

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]