#!/usr/bin/env bash
staging_location=~/tmp/unittests
mkdir -p $staging_location
cp src/*.py $staging_location
cp test/*.py $staging_location

cd $staging_location

# python3 -m pip install --user virtualenv
python -m venv unittestenv
source unittestenv/bin/activate
pip install coverage
python -m coverage run calculator_tests.py
python -m coverage report *.py
rm -rf $staging_location

