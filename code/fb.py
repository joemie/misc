import requests
import json
response = requests.get('https://graph.facebook.com/search?q=mark&type=user&access_token=[access_token]').text
data = json.loads(response)
print data['error']