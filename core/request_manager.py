"""This module provides a RequestManager for handling HTTP requests."""

import requests
from fake_useragent import UserAgent


class RequestManager:
    """This RequestManager class manages HTTP requests with user-agent, timeout, and proxy."""

    def __init__(self):
        self.ua = UserAgent()
        self.headers = {"User-Agent": self.ua.random}
        self.timeout = 10
        self.proxy = None

    def get(self, url: str) -> requests.Response:
        """Sends a GET request to the given URL."""
        if self.proxy:
            response = requests.get(
                url=url, headers=self.headers, timeout=self.timeout, proxies=self.proxy
            )
        else:
            response = requests.get(url=url, headers=self.headers, timeout=self.timeout)

        return response

    def set_proxy(self, proxy: dict) -> None:
        """Sets a proxy for future requests."""
        self.proxy = proxy
