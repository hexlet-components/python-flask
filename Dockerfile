FROM python:3.10-slim

RUN apt-get update && apt-get install make -yq

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

COPY . .

CMD ["bash", "-c", "make prod"]