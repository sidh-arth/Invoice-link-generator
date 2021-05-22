import requests, json


def generate_short_url(**kwargs):
    bitly_token = kwargs.get('bitly_token',None)
    bitly_group = kwargs.get('bitly_group',None)
    unique_link = kwargs.get('unique_link',None)
    short_link = None
    headers = { 'Authorization': 'Bearer '+bitly_token, 'Content-Type': 'application/json' }
    data = '{ "long_url":"'+ unique_link+'", "domain": "bit.ly", "group_guid": "'+bitly_group+'" }'
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

    if response.status_code == 201 or response.status_code == 200:
        short_link = response.json()
        return short_link['link']
    return short_link