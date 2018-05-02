from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mastertables',
    version='1.0.0',  # should comply with https://semver.org/
    description='A Python package to interact with the mastertables.athento.com public API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/athento/mastertables',
    author='Athento',
    author_email='adm@athento.com',
    keywords='api rest mastertables development data athento',
    install_requires=['requests'],
    packages=['mastertables'],

    entry_points={
        'console_scripts': [
            'mastertables = mastertables.help:help',
        ],
    },

    project_urls={
        'Athento': 'https://athento.com',
        'Mastertables': 'https://mastertables.athento.com',
        'Bug Reports': 'https://github.com/athento/mastertables/issues',
    },

    # Development status values:
    #   1 - Planning
    #   2 - Pre-Alpha
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    #   6 - Mature
    #   7 - Inactive
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'Operating System :: OS Independent',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
