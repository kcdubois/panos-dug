FROM python:3.10.5-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry

WORKDIR /app
COPY worker poetry.lock pyproject.toml ./

RUN poetry install --no-root

ENTRYPOINT [ "panos-worker" ]
CMD [ "run" ]