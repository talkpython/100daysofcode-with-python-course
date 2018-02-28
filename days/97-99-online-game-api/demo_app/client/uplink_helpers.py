import uplink
from requests import Response


class FormatError(Exception):
    pass


@uplink.response_handler
def raise_for_status(response: Response):
    response.raise_for_status()
    return response


@uplink.response_handler
def response_to_data(response: Response):
    try:
        return response.json()
    except Exception as x:
        raise FormatError("Invalid format, could not parse JSON. Error: {}, status={}, text={}".format(
            x, response.status_code, response.text
        )) from x
