# Rabbot

![Rabbot Logo](./assets/rabbot.png "Rabbot")

[![Build Status](https://cloud.drone.io/api/badges/dsudduth/rabbot/status.svg)](https://cloud.drone.io/dsudduth/rabbot)

A utility for validating connections to RabbitMQ servers.

## Installing Rabbot

```bash
pip install rabbot
```

## Development

This project relies on [Poetry](https://poetry.eustace.io/) for development, packaging, and publishing. You will need to have this tool installed on your machine before you can properly develop against Rabbot.

```bash
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

Please see the [installation](https://poetry.eustace.io/docs/#installation) guide for other options.


## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Versioning

This project uses semantic versioning ([SemVer 2.0.0](https://semver.org/)). Incrementing versions is managed by [bumpversion](https://github.com/peritus/bumpversion).

To ensure that the repo is properly versioned, you will need to install `bumpversion`.

```bash
pip install bumpversion
```

Once installed, bump the version before pushing your code or created a pull request.

```bash
# Examples

# Bumping the major version to indicate a backwards incompatible change
bumpversion major

# Bumping the minor version
bumpversion minor

# Bumping the subminor due to a hotfix
bumpversion patch
```

*Note: Bumpversion is configured to automatically create a commit when executed.*
