import configparser
import os

_CONFIG_ = None

def init_config(filename):
    global _CONFIG_
    ok = False
    if not _CONFIG_:
        _CONFIG_ = configparser.ConfigParser()
        if len(_CONFIG_.read(filename)) > 0:
            print('Configuration file {0} successfully loaded !'.format(filename))
            ok = True
        else:
            print("Configuration file {0} can't be loaded !".format(filename))
    else:
        print('Configuration file has already been loaded !')
    return ok

def getenv(env_var):
    return os.getenv(varname, None)

def config(section, option, env_var=None):
    res = None
    # try to search for environement var if not None
    if env_var:
        res = getenv(env_var)
    # then search in INI config if env var not found
    if not res:
        if _CONFIG_:
            if section in _CONFIG_.sections():
                if option in _CONFIG_[section]:
                    res = _CONFIG_[section][option]
                else:
                    print("Missing option {0} in section {1} in configuration file !".format(option, section))
            else:
                print("Missing section {0} in configuration file".format(section))
        else:
            print("Configuration file must be loaded to use config(section, option) function ! Call init_config(filename) before !")
    # finally return res
    return res
