import requests

headers = {'Authorization': 'Token be53b98de687f6c3715cd3244ee30ae7fc2e85be'} #be53b98de687f6c3715cd3244ee30ae7fc2e85be
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)
print(resultado.json())

# Teste endpoint correto:
assert resultado.status_code == 200 #Se URI estiver incorreta, mostrará erro

# Teste qtde de registros:
#assert resultado.json()['count'] == 2

# Teste de título do primeiro registro
#assert resultado.json()['results'][0]['titulo'] == 'Título teste'