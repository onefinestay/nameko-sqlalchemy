#!/usr/bin/env python
from setuptools import setup

setup(
    name='nameko-sqlalchemy',
    version='1.5.0',
    description='SQLAlchemy dependency for nameko services',
    author='onefinestay',
    author_email='engineering@onefinestay.com',
    url='http://github.com/onefinestay/nameko-sqlalchemy',
    packages=['nameko_sqlalchemy'],
    install_requires=[
        "nameko>=2.0.0",
        "sqlalchemy"
    ],
    extras_require={
        'dev': [
            "coverage==4.5.3",
            "flake8==3.7.7",
            "pylint>=1.9.4",  # pinned for py27 support
            "pytest==4.3.1",
            "requests==2.21.0",
            "PyMySQL",
        ]
    },
    entry_points={
        'pytest11': [
            'nameko_sqlalchemy=nameko_sqlalchemy.pytest_fixtures'
        ]
    },
    zip_safe=True,
    license='Apache License, Version 2.0',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",

    ]
)
