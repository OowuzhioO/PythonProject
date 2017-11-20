import requests

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)
# r = requests.get('https://github.com/timeline.json')

# print(r.text)
# print('=' * 200)
# print(r.content)

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

print(r.headers)