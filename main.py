from spotify.client import get_auth_code, get_access_token, get_data

def main():
    get_auth_code()
    auth_code = input('Enter the authorization code from the URL: ')
    access_token = get_access_token(auth_code)
    if access_token:
        print('Successfully obtained access token.')
        get_data(access_token)
    else:
        print('Failed to retrieve access token.')

if __name__ == '__main__':
    main()
