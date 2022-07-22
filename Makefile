install:
	poetry install

run:
	env FLASK_APP=hello_world.py \
	FLASK_ENV=development \
        poetry run python -m flask run

prod:
	poetry run gunicorn --workers=4 --bind=127.0.0.1:5000 hello_world:app
