from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()


setup(
    name='delegatable',
    packages=['delegatable'],
    version='0.0.2',
    license='MIT',
    # dependencies
    # install_requires=[],
    author='suzukimilanpaak',
    author_email='sin.wave808@gmail.com',
    url='https://github.com/suzukimilanpaak/delegatable',
    description="Delegatable is a simple Python alternative to Ruby on Rails' delegate module.",
    # read from README.md
    long_description=long_description,
    long_description_content_type='text/markdown',
    # Search keyword on PyPI
    keywords='delegate delegates delegatable delegation ruby rails',
    # https://pypi.org/classifiers/
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)
