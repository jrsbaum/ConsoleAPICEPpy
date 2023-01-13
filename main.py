import requests

def get_endereco_por_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    response = requests.get(url)
    data = response.json()

    endereco = {
        "cep": data["cep"],
        "logradouro": data["logradouro"],
        "bairro": data["bairro"],
        "localidade": data["localidade"],
        "uf": data["uf"]
    }
    return endereco

cep = input("Por favor, digite um CEP: ")
endereco = get_endereco_por_cep(cep)
print(f"CEP: {endereco['cep']}")
print(f"Logradouro: {endereco['logradouro']}")
print(f"Bairro: {endereco['bairro']}")
print(f"Localidade: {endereco['localidade']}")
print(f"UF: {endereco['uf']}")