run: 
	poetry run python move_nl_house_listing_tracker

list: 
	poetry run python move_nl_house_listing_tracker list

detail: 
	poetry run python move_nl_house_listing_tracker detail

cache: 
	poetry run python move_nl_house_listing_tracker cache

install:
	poetry install

env: FORCE
	cp example.env .env

push:
	git remote | xargs -L1 git push --all
