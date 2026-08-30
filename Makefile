.PHONY: install test run docker-build docker-run docker-test clean

IMAGE_NAME := data-engineering-demo

# Install dependencies
install:
	python -m pip install -r requirements.txt

# Run tests
test:
	python -m pytest -q

# Run the application
run:
	python src/main.py

# Build the Docker image
docker-build:
	docker build -t $(IMAGE_NAME) .

# Run the application inside Docker
docker-run:
	docker run -it --rm $(IMAGE_NAME)

# Run the test suite inside Docker
docker-test:
	docker run --rm $(IMAGE_NAME) python -m pytest -q

# Clean generated files
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache

# Format Python code to help with code structure
format:
	python -m black src tests

# Lint Python code for identifying code problems (e.g. unused packages or variables)
lint:
	python -m ruff check src tests