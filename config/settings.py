# config/settings.py

import yaml

with open("config/config.yaml") as f:
    CONFIG = yaml.safe_load(f)