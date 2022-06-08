import sys
import requests

try:
    response = requests.get("https://127.0.0.1/void")
    response.raise_for_status()
except Exception as ex:
    raise Exception("fail: %s" % str(ex))