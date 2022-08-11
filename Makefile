PORT ?= 8000

install:
	poetry install

lint:
	poetry run flake8

test:
	poetry run pytest -vv tests

check: test lint

run:
	env FLASK_APP=hello_world.py \
	FLASK_ENV=development \
        poetry run python -m flask run

requirements.txt:
	poetry export -f requirements.txt -o requirements.txt

prod:
	poetry run gunicorn --workers=4 --bind 0.0.0.0:$(PORT) hello_world:app --log-file -
