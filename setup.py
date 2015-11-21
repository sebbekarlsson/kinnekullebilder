import os
from setuptools import setup


setup(
    name='Kinnekullebilder',
    version='1.0',
    description='Website for kinnekullebilder.com',
    author='Sebastian Robert Karlsson',
    author_email='sebbekarlsson97@gmail.com',
    url='http://www.ianertson.com/',
    install_requires=[
        'flask',
        'flask-wtf',
        'wtforms',
        'PyMySQL'
    ]
)