import requests

def get_endereco_por_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()

    endereco = {
        "cep": data["cep"],
        "logradouro": data["logradouro"],
        "bairro": data["bairro"],
        "localidade": data["localidade"],
        "uf": data["uf"]
    }
    return endereco

while True:
    cep = input("Por favor, digite um CEP: ")
    endereco = get_endereco_por_cep(cep)
    if endereco is None:
        print("CEP inválido. Por favor, tente novamente.")
    else:
        print(f"CEP: {endereco['cep']}")
        print(f"Logradouro: {endereco['logradouro']}")
        print(f"Bairro: {endereco['bairro']}")
        print(f"Localidade: {endereco['localidade']}")
        print(f"UF: {endereco['uf']}")
        break