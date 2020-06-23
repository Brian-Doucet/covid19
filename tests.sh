#!/bin/bash

# Call pytest for testing suite
pytest -v --disable-pytest-warnings \

# Show which statements are missing coverage
--cov-report=term-missing \

# Directory to call pytest on
tests
