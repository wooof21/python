


import requests

r = requests.get('https://api.github.com/users/codewithharry')

with open("codewithharry.json", "w") as f:
    f.write(r.text)