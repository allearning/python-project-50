install:
	poetry install

gen-diff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -s

test-cov:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
