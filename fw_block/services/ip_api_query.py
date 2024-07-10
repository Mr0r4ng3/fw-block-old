import requests
from fw_block.settings import IP_API_URL


error_reasons = {
    "Invalid IP address": "Invalid IP address",
    "Reserved IP address": "Reserved IP address",
}


def query_ip_in_api(ip: str) -> dict:

    data = None

    try:

        url = f"{IP_API_URL}/{ip}/json/"
        response: dict = requests.get(url).json()

        if response.get("error"):

            error = response.get("reason")

            data = {"error": True, "reason": error_reasons.get(error, error)}

        else:

            data = response

    except requests.exceptions.ConnectionError:

        data = {"error": True, "reason": "Connection to API failed"}

    return data
