# Mastertables

[![Website](https://img.shields.io/website-up-down-green-red/http/shields.io.svg?label=website&style=for-the-badge)](https://mastertables.athento.com)
[![PyPI](https://img.shields.io/pypi/v/mastertables.svg?style=for-the-badge)](https://pypi.org/project/mastertables)
[![PyPI - Status](https://img.shields.io/pypi/status/mastertables.svg?style=for-the-badge)](https://pypi.org/project/mastertables)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mastertables.svg?style=for-the-badge)](https://pypi.org/project/mastertables)

A Python package to interact with [Mastertables](https://mastertables.athento.com).

This package provides a very simple way of getting data from your mastertables through the public *Rest API*.

## Installation

### Install from PyPI (recommended)

Just run the command below from the CLI:

```shell
pip install mastertables
```

To add the package to your local `requirements.txt` run:

```shell
pip freeze > requirements.txt
```

### Install from repo

You can install Mastertables from the Github repo:

```shell
pip install git+https://github.com/athento/mastertables
```

### Install from source

Alternatively, you can even install it from the sources:

```shell
git clone https://github.com/athento/mastertables
cd mastertables
pip install .
```

## Updating

### Update from PyPI

```shell
pip install mastertables --upgrade
```

### Update from repo

```shell
pip install git+https://github.com/athento/mastertables --upgrade
```

### Update from source

```shell
cd /path/to/mastertables/repo
git pull
pip install . --upgrade
```

## API reference

```python
# module
from mastertables import mastertables


# mastertables client instantiation
# usage:
#   mastertables.MasterTablesClient("<team_api_key>")

mt = mastertables.MasterTablesClient("OAIV9839AF893H923ONWAN3IGNAWNAUNEGIU")


# get vocabulary
# usage:
#   mastertables.MasterTablesClient.get_vocabulary("<vocabulary_uuid>" [, category="<category>"])
# output:
#   {u'foo': u'bar', u'asdf': u'qwer'}

print(mt.get_vocabulary("1234abcd-12ab-34cd-56ef-12345678abcd"))


# get vocabulary reverse (value:key, instead of key:value)
# usage:
#   mastertables.MasterTablesClient.get_vocabulary_reverse("<vocabulary_uuid>" [, category="<category>"])
# output:
#   {u'bar': u'foo', u'qwer': u'asdf'}

print(mt.get_vocabulary_reverse("1234abcd-12ab-34cd-56ef-12345678abcd"))


# get vocabulary values
# usage:
#   mastertables.MasterTablesClient.get_values("<vocabulary_uuid>")
# output:
#   [u'foo', u'asdf']

print(mt.get_values("1234abcd-12ab-34cd-56ef-12345678abcd"))


# get vocabulary entity value
# usage:
#   mastertables.MasterTablesClient.get_value("<vocabulary_uuid>", "<entity_key>" [, index=<index>])
# output:
#   u'bar'

print(mt.get_value("1234abcd-12ab-34cd-56ef-12345678abcd", "foo", 0))
```

## Packaging and distributing

[Click on this link](https://github.com/athento/mastertables/blob/master/PACKAGING.md) to read the manual on how to package and upload mastertables to PyPI.
