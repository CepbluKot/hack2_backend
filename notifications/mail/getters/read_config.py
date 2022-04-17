import json


with open('config.json') as file:
    config = json.load(file)


def get_email():
    return config["my_email"]


def get_post_server_address():
    return config["post_server_address"]


def get_password():
    return config["email_password"]
    