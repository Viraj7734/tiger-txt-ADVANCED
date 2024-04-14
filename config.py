import os

API_ID = API_ID = 28828575

API_HASH = os.environ.get("API_HASH", "df26b09fa8d1ffa35fbfc1ad41d86bad)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6761706865:AAE2vAsAjBfBkZko2uxhYkOEPUq1ltmfT6c")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5946310116)

LOG = -1001993688323

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


