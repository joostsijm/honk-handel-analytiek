run: 
	poetry run python move_nl_house_listing_tracker

install:
	poetry install

env: FORCE
	cp example.env .env
