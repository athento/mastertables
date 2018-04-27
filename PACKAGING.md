# Packaging and distributing

## Dependencies

First of all, install the dependencies needed to publish the package to PyPi:

```shell
pip install twine
pip install wheel
```

- [twine](https://pypi.org/project/twine/): used to upload the project distribution to PyPi.
- [wheel](https://pypi.org/project/wheel/): used to build wheels for the project. A wheel is a built package that can be installed without needing to go through the "*build*" process.

## Updating package info

Before building the new distribution version, update the following fields in `setup.py`:

## Building

### Source distribution

*Source distributions* are unbuilt, and require a build step when installed by pip.

```shell
python setup.py sdist
```

### Universal wheel

Universal wheels are pure Python distributions (with no compiled extensions) that natively support both Python 2 and 3.

```shell
python setup.py bdist_wheel --universal
```

### Pure Python wheel

Pure Python wheels are pure Python distributions that only support one Python version, either 2 or 3.

```shell
python setup.py bdist_wheel
```

### Platform wheel

Platform wheels are wheels that are specific to a certain platform like Linux, macOS, or Window, usually due to containing compiled extensions.

```shell
python setup.py bdist_wheel
```

## Distributing

After building the project, a new folder should be created at `dist/`, containing the packaged project. Run the command below to upload your distribution to PyPi.

```shell
twine upload dist/*
```

> You will need credentials in order to be able to upload the package.
