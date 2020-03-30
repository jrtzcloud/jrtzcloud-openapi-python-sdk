import setuptools  # important
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

extensions = []
extensions.append(Extension('BltenClient', ['blten/v20191120/blten_client']))
extensions.append(Extension('JrtzCloudSDKException', ['common/exception/jrtzcloud_sdk_exception.py']))

setup(
    ext_modules=cythonize(extensions, compiler_directives={'language_level': 2}),
)