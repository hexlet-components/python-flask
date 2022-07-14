run:
	env FLASK_APP=hello_world.py \
	FLASK_ENV=development \
        poetry run python -m flask run
