import requests

URL = "http://127.0.0.1:3005"


def request_data(url):
    response = requests.get(url)
    response_json = response.json()
    return response_json


def get_user_by_id(id):
    return request_data(URL + "/" + str(id))


def get_all_users():
    return request_data(URL + "/")


def get_user_role(id):
    return request_data(URL + "/" + str(id) + "/role")


def get_user_position(id):
    return request_data(URL + "/" + str(id) + "/position")


def get_user_platform(id):
    return request_data(URL + "/" + str(id) + "/platform")


def get_all_positions():
    return request_data(URL + "/positions")


def get_all_roles():
    return request_data(URL + "/roles")
