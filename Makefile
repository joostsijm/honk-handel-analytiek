run: 
	poetry run python honk-handel-tracker

install:
	poetry install

env: FORCE
	cp example.env .env
