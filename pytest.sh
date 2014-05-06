#!/bin/sh
cd graph/
python -m unittest discover
rm *.pyc
cd ../ad
python -m unittest discover
rm *.pyc
cd ../
