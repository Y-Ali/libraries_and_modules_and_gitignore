import requests

requests_websites = requests.get("https://pypi.org/project/requests/")
print(requests_websites.status_code)
