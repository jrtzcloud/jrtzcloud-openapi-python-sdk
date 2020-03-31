#!/usr/bin/bash

python setup.py sdist
cd dist/
tar -zxvf jrtzcloud-python-sdk-core-1.0.0.tar.gz
cd jrtzcloud-python-sdk-core-1.0.0
python setup.py install