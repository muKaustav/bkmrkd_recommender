FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["celery", "-A", "worker.celery", "worker", "--loglevel=info", "--concurrency=4"]
