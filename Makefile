.PHONY:	install run

install:
	pipenv install --dev --pre

lint:
	flake8 .
	black --check -t py37 .

format:
	black -t py37 .

run:
	pipenv run scrapy crawl room
