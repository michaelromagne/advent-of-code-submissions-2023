SHELL :=/bin/bash
.PHONY: all test coverage black flake8
.SILENT:

all:
	echo "Usage :"
	echo "      make test"           # Run tests
	echo "      make coverage"           # Run tests and coverage
	echo "      make black"          # Run black formatter on python code
	echo "      make flake8"          # Run flake8 linter on python code
	echo "      make isort"          # Run isort linter on python code

test:
	pipenv run pytest --disable-pytest-warnings tests -vvv

coverage:
	pipenv run coverage run --source ml-detector -m pytest --disable-pytest-warnings && pipenv run coverage report --fail-under=80

black:
	pipenv run black .

flake8:
	pipenv run flake8

isort:
	pipenv run isort **/*.py

# SkyPilot commands
sky_status:
	pipenv run sky status --refresh

# Launch a cluster that will autostop after 120 minutes of idleness
sky_launch:
	pipenv run sky launch -c $(cluster_name) $(sky_manifest) -i 120

sky_exec:
	pipenv run sky exec $(cluster_name) $(sky_manifest)

sky_down:
	pipenv run sky down $(cluster_name)

sky_stop:
	pipenv run sky stop $(cluster_name)
