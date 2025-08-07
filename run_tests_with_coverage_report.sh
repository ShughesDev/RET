#!/usr/bin/env sh
# This is a script to run the tests 3 times, once to write the coverage of each specific module.

pytest ret/testsret --cov=ret/ret --cov-report=html:htmlcov/ret-coverage
pytest ret/testsret --cov=ret/retgen --cov-report=html:htmlcov/retgen-coverage
pytest ret/testsret --cov=ret/retplay --cov-report=html:htmlcov/retplay-coverage

read -p "Test script has finished. Press any key to continue"
