from httplib2 import Http
from json import dumps

#
# Hangouts Chat incoming webhook quickstart
#
def main():
    url = 'https://chat.googleapis.com/v1/spaces/AAAAQZCR_rU/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=VqS7uSAWxw1CDtPyZ7cLJknYSnD7gHothmxVpNjPBys%3D'
    bot_message = {
        'text' : 'push on master branch'}
    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )





    print(response)

if __name__ == '__main__':
    main()
