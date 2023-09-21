from os import getenv


api_id = int(getenv("api_id"))
api_hash = getenv("api_hash")

session = getenv("session", None)

SUDO_USER = list(map(int, getenv("SUDO_USER", "2063166406").split()))
