#!/usr/bin/env bash
pip install pyinstaller

filename=orders.csv
if [ ! -f $filename ]
then
	touch $filename
fi

pyinstaller --onefile --name llm myls.py

cp dist/llm .

rm -rf __pycache__ build dist llm.spec

