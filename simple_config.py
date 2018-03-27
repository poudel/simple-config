import os
import json


class Config:
    """
    This class is intended to be instantiated once used as a singleton throughout
    your application. See the README.md for more information.

    Quick example:

    >>>from simple_config import Config
    >>>settings = Config("/path/to/config.json", defaults={"is_true": True})
    >>>if settings.is_true:
    >>>    print("Is very true")
    Is very true

    """

    def __init__(self, path, defaults=None):
        self.path = path
        self.defaults = defaults or {}

        if not os.path.exists(self.path):
            with open(self.path, "w") as buff:
                buff.write(json.dumps(self.defaults))

        with open(self.path, "r") as buff:
            self.config = json.loads(buff.read())

    def update(self, **kwargs):
        """
        Update config parameters and save them to file for persistence
        """
        self.config.update(**kwargs)

        with open(self.path, "w") as buff:
            buff.write(json.dumps(self.config))
        return self.config

    def __getattr__(self, name):
        if name in self.config.keys():
            return self.config[name]
        else:
            raise AttributeError("Config parameter was not found!")
