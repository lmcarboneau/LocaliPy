"""
Placeholder


"""

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    # users should be able to install using
    # $ pip install localipy
    name='localipy',
    version='0.1',
    description='A Python 3 module for extracting locations from input text',
    long_description=long_description, # from README; see above
    url='https://github.com/lmcarboneau/LocaliPy',
    packages=find_packages()
)