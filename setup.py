#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='cooperhewitt.roboteyes.colors',
    namespace_packages=['cooperhewitt', 'cooperhewitt.roboteyes'],
    version='0.1',
    description='',
    author='Cooper Hewitt Smithsonian Design Museum',
    url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-colors',
    install_requires=['roygbiv'],
    packages=packages,
    scripts=[],
    download_url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-colors/releases/tag/v0.1',
    license='BSD')
