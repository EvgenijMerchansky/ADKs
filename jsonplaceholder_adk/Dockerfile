FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY jsonplaceholder_adk /app/jsonplaceholder_adk

RUN pip install --no-cache-dir -r /app/jsonplaceholder_adk/requirements.txt

EXPOSE 8000

CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8000"]