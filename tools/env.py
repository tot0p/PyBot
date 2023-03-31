#-*- coding: utf-8 -*-

import os

def LoadEnv():
    """Load environment variables from .env file if it exists."""
    if os.path.isfile('.env'):
        print('Importing environment from .env...')
        for line in open('.env'):
            var = line.strip().split('=')
            if len(var) == 2:
                os.environ[var[0]] = var[1]


def Get(key):
    """Get environment variable."""
    return os.environ.get(key)

def Set(key, value):
    """Set environment variable."""
    os.environ[key] = value