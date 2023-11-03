run: 
	poetry run python honk-handel-tracker

list: 
	poetry run python honk-handel-tracker list

detail: 
	poetry run python honk-handel-tracker detail

cache: 
	poetry run python honk-handel-tracker cache

install:
	poetry install

env: FORCE
	cp example.env .env

push:
	git remote | xargs -L1 git push --all
