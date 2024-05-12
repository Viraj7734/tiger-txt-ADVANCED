import os

API_ID = API_ID = 24265798

API_HASH = os.environ.get("API_HASH", "439c569744c141c6b6d727c778de60a6)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7076140541:AAE05p91LrYabpvPF-QlEZPHo6EQkHCXGjg")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7148861119)

LOG = -1002017627785

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


