import os
from ginsfsm.compat import configparser
from logging.config import fileConfig


def logging_file_config(config_file, fileConfig=fileConfig,
                        configparser=configparser):
    """
    Setup logging via the logging module's fileConfig function with the
    specified ``config_file``, if applicable.

    ConfigParser defaults are specified for the special ``__file__``
    and ``here`` variables, similar to PasteDeploy config loading.
    """
    parser = configparser.ConfigParser()
    parser.read([config_file])
    if parser.has_section('loggers'):
        config_file = os.path.abspath(config_file)
        return fileConfig(
            config_file,
            dict(__file__=config_file, here=os.path.dirname(config_file))
            )
