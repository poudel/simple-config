# Simple Config

A simple configuration file manager for python. Best suited for simple scripts that need
to take user defined configuration parameters.

Configuration is saved in JSON format to a file of your chosing.


## Why?

This is mostly intended to be used in quick and dirty scripts and simple CLI apps.
This does not intend to replace `configparser`. There are instances where I feel
that bootstrapping `configparser` is an overkill. This is where `simple_config` chips in.


## Installation

Install if using `pipenv` by running the command below.

```bash
pipenv install simple-config
```

Or, if you are not using `pipenv`, run the following:

```bash
pip install simple-config
```

## Usage

`simple-config` provides a `Config` class. It is intended to be instantiated
at the module level once and used the instance everywhere.

Put this in a file called `config.py`:

```python
from simple_config import Config

default_settings = {
    "is_registered": True,
    "token": "aK3NJe3PnXJr"
}
settings = Config("/path/to/config.json", defaults=default_settings)
```

Here, the first argument is the path to the configuration file.
The `defaults` keyword argument takes the default configuration
options for your app.
If the config file does not exist, it will be created and populated
with the default values.

Now, import the instance of `Config` i.e. `settings` wherever necessary and use:

```python
from config import settings

print(settings.token)
```

### Mutating the config

Sometimes there might be a need to update the config, e.g. to save state of
the app. The `Config` class provides `update` instance method.

```python
settings.update(token="Ju901jK1Rb")
```

The update method will update the parameters and write it to the config
file as well.


## Multiple configs

There can exist more than one `Config` instance in an application. For example,
the application auto-generated state can be saved in one file and user's config
can be saved in another instance.


## Run the tests

Go to the root of this project and run:

```python
python -m unittest discover
```
