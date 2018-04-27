# Mastertables

[![Website](https://img.shields.io/website-up-down-green-red/http/shields.io.svg?label=website&style=for-the-badge)](https://mastertables.athento.com)
[![PyPI](https://img.shields.io/pypi/v/nine.svg?style=for-the-badge)](#)
[![PyPI - Status](https://img.shields.io/pypi/status/Django.svg?style=for-the-badge)](#)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg?style=for-the-badge)](#)

A Python package to interact with [Mastertables](https://mastertables.athento.com).

This package provides a very simple way of getting data from your mastertables through the public *Rest API*.

## API

```python
# module
import mastertables

# mastertables client instantiation
# mastertables.MasterTablesClient("<team_api_key>")
mt = mastertables.MasterTablesClient("OAIV9839AF893H923ONWAN3IGNAWNAUNEGIU")

# get vocabulary
# mastertables.MasterTablesClient.get_vocabulary("<vocabulary_uuid>" [, category="<category>"])
print(mt.get_vocabulary("1234abcd-12ab-34cd-56ef-12345678abcd"))

# get vocabulary reverse (value:key, instead of key:value)
# mastertables.MasterTablesClient.get_vocabulary_reverse("<vocabulary_uuid>" [, category="<category>"])
print(mt.get_vocabulary_reverse("1234abcd-12ab-34cd-56ef-12345678abcd"))

# get vocabulary values
# mastertables.MasterTablesClient.get_values("<vocabulary_uuid>")
print(mt.get_values("1234abcd-12ab-34cd-56ef-12345678abcd"))
```
