run:
	poetry run python honk-handel-tracker

list_from_cache:
	poetry run python honk-handel-tracker list_from_cache

list:
	poetry run python honk-handel-tracker list

detail:
	poetry run python honk-handel-tracker detail

detail_from_cache:
	poetry run python honk-handel-tracker detail_from_cache

install:
	poetry install

env: FORCE
	cp example.env .env

push:
	git remote | xargs -L1 git push --all
