#!/bin/env python
import os
import requests
import argparse


parser = argparse.ArgumentParser(description='winterfell client')
parser.add_argument('action', default="create",
                    help='create or delete or get')

parser.add_argument('username', help='username')
parser.add_argument('-p', '--password', default="test",
                    help='only create user is necessery')

args = parser.parse_args()
username = args.username
password = args.password
action = args.action

headers = {'X-Auth-Token': '2016winterfell'}
user_info = {"username": username, "password": password}
winterfell_api = "http://127.0.0.1:9091"

if action == 'create':
    request_url = winterfell_api + '/user'
    response = requests.post(request_url, params=user_info, headers=headers)
elif action == 'delete':
    request_url = '%s/user/%s' % (winterfell_api, username)
    response = requests.delete(request_url, headers=headers)
elif action == 'get':
    request_url = '%s/user/%s' % (winterfell_api, username)
    response = requests.get(request_url, headers=headers)
    google_key = response.json()['google_auth_key']
    qr_str = 'otpauth://totp/%s@ci.polex.com?secret=%s&issuer=ci.polex.com.'\
        % (username, google_key)
    os.system("qrencode -t ANSI '%s'" % qr_str)

print response.text
