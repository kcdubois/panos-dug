FROM python:3.10.5-slim

RUN pip install pipenv

WORKDIR /app
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system

COPY worker .

CMD [ "app.py" ]