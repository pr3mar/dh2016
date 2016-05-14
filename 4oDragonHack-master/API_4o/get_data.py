import requests

import config
from API_4o.authorization import access_token


def get_user_by_email(user_email):
    url = '{}/user?email={}'.format(config.API_4O['URL'], user_email)

    headers = {
        'Accept': 'application/vnd.4thoffice.user-4.0+json',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US;q=1',
        'Authorization': access_token
    }

    response = requests.get(
        url,
        headers=headers
    )

    return response


def get_streams_of_user(user_id, offset=0, size=512, menu_scope='Important', group_streams_only=False):
    url = '{}/navigation?offset={}&size={}&menuScope={}&groupStreamOnly={}'.format(config.API_4O['URL'], offset, size, menu_scope, group_streams_only)

    headers = {
        'Accept': 'application/vnd.4thoffice.menu-v5.15+json',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US;q=1',
        'Authorization': access_token,
        'X-Impersonate-User': user_id
    }

    response = requests.get(
        url,
        headers=headers
    )

    return response


def get_stream(user_id, stream_id):
    url = '{}/stream/{}'.format(config.API_4O['URL'], stream_id)

    headers = {
        'Accept': 'application/vnd.4thoffice.stream-5.3+json',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US;q=1',
        'Authorization': access_token,
        'X-Impersonate-User': user_id
    }

    response = requests.get(
        url,
        headers=headers
    )

    return response


def get_group(user_id, group_id):
    url = '{}/group/{}'.format(config.API_4O['URL'], group_id)

    headers = {
        'Accept': 'application/vnd.4thoffice.group-5.3+json',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US;q=1',
        'Authorization': access_token,
        'X-Impersonate-User': user_id
    }

    response = requests.get(
        url,
        headers=headers
    )

    return response
