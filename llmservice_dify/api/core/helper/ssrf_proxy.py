"""
Proxy requests to avoid SSRF
"""

import logging
import os
import time

import httpx

SSRF_PROXY_ALL_URL = os.getenv("SSRF_PROXY_ALL_URL", "")
SSRF_PROXY_HTTP_URL = os.getenv("SSRF_PROXY_HTTP_URL", "")
SSRF_PROXY_HTTPS_URL = os.getenv("SSRF_PROXY_HTTPS_URL", "")
SSRF_DEFAULT_MAX_RETRIES = int(os.getenv("SSRF_DEFAULT_MAX_RETRIES", "3"))

proxy_mounts = (
    {
        "http://": httpx.HTTPTransport(proxy=SSRF_PROXY_HTTP_URL),
        "https://": httpx.HTTPTransport(proxy=SSRF_PROXY_HTTPS_URL),
    }
    if SSRF_PROXY_HTTP_URL and SSRF_PROXY_HTTPS_URL
    else None
)

BACKOFF_FACTOR = 0.5
STATUS_FORCELIST = [429, 500, 502, 503, 504]


def make_request(method, url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    if "allow_redirects" in kwargs:
        allow_redirects = kwargs.pop("allow_redirects")
        if "follow_redirects" not in kwargs:
            kwargs["follow_redirects"] = allow_redirects

    retries = 0
    while retries <= max_retries:
        try:
            if SSRF_PROXY_ALL_URL:
                with httpx.Client(proxy=SSRF_PROXY_ALL_URL) as client:
                    response = client.request(method=method, url=url, **kwargs)
            elif proxy_mounts:
                with httpx.Client(mounts=proxy_mounts) as client:
                    response = client.request(method=method, url=url, **kwargs)
            else:
                with httpx.Client() as client:
                    response = client.request(method=method, url=url, **kwargs)

            if response.status_code not in STATUS_FORCELIST:
                return response
            else:
                logging.warning(f"Received status code {response.status_code} for URL {url} which is in the force list")

        except httpx.RequestError as e:
            logging.warning(f"Request to URL {url} failed on attempt {retries + 1}: {e}")

        retries += 1
        if retries <= max_retries:
            time.sleep(BACKOFF_FACTOR * (2 ** (retries - 1)))

    raise Exception(f"Reached maximum retries ({max_retries}) for URL {url}")


def get(url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    return make_request("GET", url, max_retries=max_retries, **kwargs)


def post(url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    return make_request("POST", url, max_retries=max_retries, **kwargs)


def put(url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    return make_request("PUT", url, max_retries=max_retries, **kwargs)


def patch(url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    return make_request("PATCH", url, max_retries=max_retries, **kwargs)


def delete(url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    return make_request("DELETE", url, max_retries=max_retries, **kwargs)


def head(url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    return make_request("HEAD", url, max_retries=max_retries, **kwargs)
