FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY agents/posts/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY agents/posts/ /app/posts/

ENV PYTHONPATH=/app

WORKDIR /app/posts

EXPOSE 8000

CMD ["uvicorn", "main:a2a_app", "--host", "0.0.0.0", "--port", "8000"]