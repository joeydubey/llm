#!/usr/bin/env bash

python -m unittest discover

rm -rf test.csv __pycache__ test/__pycache__