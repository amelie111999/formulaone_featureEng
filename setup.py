# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='load_movie_data',
    version='0.1.0',
    description='Downloads and prepares formula one data',
    long_description=readme,
    author='Amelie Schueler',
    author_email='amelie.schueler@stud.h-da.de',
    url='https://github.com/kennethreitz/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
