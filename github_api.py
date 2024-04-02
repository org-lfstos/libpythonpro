import requests
import json


def buscar_avatar(usuario):
    """Busca o avatar de um usuário no Github"""

    url = f'https://api.github.com/users/{usuario}'
    response = requests.get(url)
    return json.loads(response.text)['avatar_url']


print(buscar_avatar('lfstos'))
