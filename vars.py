import sys
from os import environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
        )
PING_INTERVAL = int(environ.get("PING_INTERVAL", "30"))  # 30 Seconds
