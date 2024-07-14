import json
from json import JSONDecodeError

import requests
from requests.models import Response
from tests import config

logger = config.get_logger("test_rest_client")


def _init_request(uri: str, headers: dict):
    base_url = config.get("crate.serviceHost")
    apikey = config.get("crate.apikey")
    full_uri = f"{base_url}{'' if base_url.endswith('/') else '/'}{'account-dog-service'}{'' if uri.startswith('/') else ''}{uri}"

    headers["apikey"] = apikey
    return full_uri, headers


def get_request(uri: str, headers: dict):
    full_uri, headers = _init_request(uri, headers)

    logger.info(f"Getting data to {full_uri} with headers {headers}")
    resp: Response = requests.get(full_uri, headers=headers)

    return resp.status_code, resp.json()


def post_request(uri: str, headers: dict, body: dict):
    full_uri, headers = _init_request(uri, headers)

    logger.info(f"Posting data to {full_uri} with headers {headers}")
    logger.info(json.dumps(body))
    resp: Response = requests.post(full_uri, headers=headers, data=json.dumps(body))
    content = resp.text
    try:
        content = resp.json()
    except JSONDecodeError:
        logger.info("The response is not json")
    return resp.status_code, content


def put_request(uri: str, headers: dict, body: dict):
    full_uri, headers = _init_request(uri, headers)
    resp: Response = requests.put(full_uri, headers=headers, data=json.dumps(body))
    content = resp.text
    try:
        content = resp.json()
    except JSONDecodeError:
        logger.info("The response is not json")
    return resp.status_code, content


def patch_request(uri: str, headers: dict, body: dict):
    full_uri, headers = _init_request(uri, headers)

    logger.info(f"Patching data to {full_uri} with headers {headers}")
    logger.info(json.dumps(body))
    resp: Response = requests.patch(full_uri, headers=headers, data=json.dumps(body))
    content = resp.text
    try:
        content = resp.json()
    except JSONDecodeError:
        logger.info("The response is not json")
    return resp.status_code, content


def delete_request(uri: str, headers: dict):
    full_uri, headers = _init_request(uri, headers)

    logger.info(f"Deleting data to {full_uri} with headers {headers}")
    resp: Response = requests.delete(full_uri, headers=headers)
    content = resp.text
    try:
        content = resp.json()
    except JSONDecodeError:
        logger.info("The response is not json")
    return resp.status_code, content
