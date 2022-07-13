FROM python:3.10.5-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.dev.txt .
RUN pip install -r requirements.dev.txt

COPY setup.py .
COPY worker ./worker

RUN pip install -e .

ENTRYPOINT [ "panos-worker" ]
CMD [ "run" ]