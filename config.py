import configparser, os

config = configparser.ConfigParser()

for loc in os.curdir, os.path.expanduser("~/.config"), "/etc/openhr20-query", os.environ.get("OPENHR20_CONF"):
    try:
        if (loc is not None):
            with open(os.path.join(loc,"openhr20-query.ini")) as source:
                config.readfp(source)
    except IOError:
        pass