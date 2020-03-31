#!/usr/bin/bash

rm -rf dist jrtzcloud_python_sdk_core.egg-info
python setup.py sdist
cd dist/
tar -zxvf jrtzcloud-python-sdk-core-1.0.0.tar.gz
cd jrtzcloud-python-sdk-core-1.0.0
python setup.py install