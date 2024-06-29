import os
import json
import requests
import urllib.parse
from dotenv import load_dotenv
from util.util import parse_data

load_dotenv()

redirect_uri='http://localhost:3000'

def get_auth_code():
    try: 
        url = 'https://accounts.spotify.com/authorize'
        scope = 'user-read-private user-read-email'
        params = {
            'client_id': os.getenv('client_id'),
            'response_type': 'code',
            'redirect_uri': redirect_uri,
            'scope': scope
        }
        auth_url = f"{url}?{urllib.parse.urlencode(params)}"
        print('Visit this URL to authorize the application:', auth_url)
    except Exception as e:
        print(f'Error generating authorization URL: {e}')

def get_access_token(code):
    url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_secret': os.getenv('client_secret'),
        'client_id': os.getenv('client_id')
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            data = response.json()
            token = data.get('access_token')
            return token
        else:
            print('Failed to obtain access token', response.status_code, response.text)
    except:
        print('Error getting access token.')

def get_data(token):
    url = 'https://charts-spotify-com-service.spotify.com/auth/v0/charts/regional-global-weekly/latest'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            parsed_data = parse_data(data)
            with open('data.json', 'w') as f:
                json.dump(parsed_data, f, indent=4)
                print('Successfully created data.json.')
        else:
            print('Failed to get data:', response.status_code, response.text)
    except:
        print('Error getting data.')