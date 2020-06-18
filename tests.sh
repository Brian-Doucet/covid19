#!/bin/bash

# Call pytest for testing suite
pytest -v --disable-pytest-warnings \

# Show coverage report in the terminal
--cov-report term --cov=covid19 \

# Show which statements are missing coverage
--cov-report=term-missing \

# Directory to call pytest on
tests
