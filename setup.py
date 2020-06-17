import os.path
from codecs import open
from setuptools import setup, find_packages


here = os.path.dirname(__file__)
readme_path = os.path.join(here, 'README.md')
readme = open(readme_path).read()


setup(
    # General Info
    name='delegable',
    version='0.0.5',
    license='MIT',
    author='suzukimilanpaak',
    author_email='sin.wave808@gmail.com',
    url='https://github.com/suzukimilanpaak/delegable',
    description="Delegable is a simple Python alternative to Ruby on Rails' delegate module.",
    long_description=readme,
    long_description_content_type='text/markdown',
    # Search keyword on PyPI
    keywords='delegate delegates delegable delegation ruby rails',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,

    # https://pypi.org/classifiers/
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],

    # Dependencies
    install_requires=[
        'setuptools >= 0.7'
    ],
    extras_require={
        'testing': [
            'flake8==3.8.2',
            'pytest==5.4.3',
            'pytest-cov==2.9.0',
            'pytest-flake8==1.0.6',
            'pytest-mock==3.1.0',
            'pytest-describe==1.0.0'
        ]
    }
)
