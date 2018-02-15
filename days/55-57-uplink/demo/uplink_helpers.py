import uplink


@uplink.response_handler
def raise_for_status(response):
    response.raise_for_status()
    return response
