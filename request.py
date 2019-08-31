# -*- encoding: utf-8 -*-

import requests


def use_simple_requests(url):
    res = requests.get(url)
    print(">>>>Response Headers")
    print(res.headers)
    print(">>>>Response body")
    print(res.text)


def user_data_requests(url):
    params = {'param1': 'hello', 'param2': 'word'}
    res = requests.get(url, params=params)
    print(">>>>Response headers")
    print(res.headers)
    print(">>>>Response status_code")
    print(res.status_code)
    print(">>>>Response json")
    print(res.json())


if __name__ == "__main__":
    url = "http://httpbin.org"
    use_simple_requests(url)
    url_get = "http://httpbin.org/get"
    user_data_requests(url_get)
