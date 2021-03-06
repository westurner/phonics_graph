#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pyyaml',
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest-cov', 'pytest>=3', ]

setup(
    author="Wes Turner",
    author_email='wes@wrd.nu',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A graph of phonics things like lexemes, phonemes, and IPA: International Phonetic Alphabet",
    entry_points={
        'console_scripts': [
            'phonics_graph=phonics_graph.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='phonics_graph',
    name='phonics_graph',
    packages=find_packages(include=['phonics_graph', 'phonics_graph.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/westurner/phonics_graph',
    version='0.1.0',
    zip_safe=False,
)
