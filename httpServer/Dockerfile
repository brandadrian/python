FROM python:3-alpine

ADD . /app

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir requests configparser

CMD ["python", "httpServer.py"]