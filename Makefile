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
        poetry run python -m flask run --host=localhost --port=8000

requirements.txt:
	poetry export -f requirements.txt -o requirements.txt

prod:
	poetry run gunicorn --workers=4 --bind=127.0.0.1:8000 hello_world:app --log-file -
