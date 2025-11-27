import requests

headers = {'Authorization': 'Token be53b98de687f6c3715cd3244ee30ae7fc2e85be'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

#curso = requests.get(url=f'{url_base_cursos}3/', headers=headers)
#print(curso.json())

resultado = requests.delete(url=f'{url_base_cursos}3/', headers=headers)
assert resultado.status_code == 204
assert len(resultado.text) == 0