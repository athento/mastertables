# Packaging and distributing

#### Prerequisites

First of all, install the dependencies needed to publish the package to PyPi:

```shell
pip install twine
pip install wheel
```

- [twine](https://pypi.org/project/twine/): used to upload the project distribution to PyPi.
- [wheel](https://pypi.org/project/wheel/): used to build wheels for the project. A wheel is a built package that can be installed without needing to go through the "*build*" process.

## 1. Update package info

Before building the new distribution version, update the following fields in `setup.py`:

- `version`: should comply with [semver.org](https://semver.org/).
    - Given a version number `MAJOR.MINOR.PATCH`, increment the:
        - `MAJOR` version when you make incompatible API changes,
        - `MINOR` version when you add functionality in a backwards-compatible manner, and
        - `PATCH` version when you make backwards-compatible bug fixes.
- `classifiers >> Development Status`: see `setup.py` for more info.

Push your changes to Github.

## 2. Create Github release

After pushing the changes, go to the Github repository and create a new release using the same `version` number you used in `setup.py`:

1. Go to the [releases page](https://github.com/athento/mastertables/releases).
2. Click on the `Draft a new release` button.
    - __Tag version__: use the same `version` number you used in `setup.py`.
    - __Release title__: use the same `version` number you used in `setup.py`.
    - __Description__: write a markdown unordered list changelog using the following keywords: `add`, `fix`, and `del`, in the same order; eg:
    - __This is a pre-release__: check this box if the release is a bleeding-edge one (not stable).

```markdown
- `add` - new superpowah ! :)
- `add` - herobrine
- `fix` - error with blah, blah, blah
- `del` - crap
- `del` - old feature...
```

## 3. Build package

*Source distributions* are unbuilt, and require a build step when installed by pip.

```shell
python setup.py sdist
```

After building the project, a new folder should be created at `dist/`, containing the packaged project.

## 4. Distribute it !

To finish it all, run the command below to upload your distribution to PyPI:

```shell
twine upload dist/*
```

You will need PyPI credentials in order to be able to upload the package.
