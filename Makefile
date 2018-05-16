bootstrap:
	pipenv sync --dev

test:
	pipenv run python -m pytest

build:
	docker build -t adder:latest .

run:
	docker run -it adder:latest

shell:
	docker run -it adder:latest bash

