run: 
	poetry run python housetrack

install:
	poetry install

env: FORCE
	cp example.env .env
