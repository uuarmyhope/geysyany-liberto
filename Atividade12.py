import requests
# Definindo o CEP que será consultado
cep = input("Digite o CEP para consulta")
# URL da API do ViaCEP
url = f"https://viacep.com.br/ws/{cep}/json/"
# Fazendo a requisição GET
response = requests.get(url)
# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
   # Convertendo a resposta para JSON
   data = response.json()
   # Exibindo os dados
   print(f"CEP: {data['cep']}")
   print(f"Logradouro: {data['logradouro']}")
   print(f"Bairro: {data['bairro']}")
   print(f"Cidade: {data['localidade']}")
   print(f"Estado: {data['uf']}")
else:
   print("Erro ao acessar a API:", response.status_code)
