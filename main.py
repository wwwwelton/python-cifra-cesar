import json
import urllib
import os.path
from os import path
import string
import hashlib
import requests

casas = 1
alfabeto = string.ascii_lowercase
decifrado = ""

url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=aca1db91a274e399134ef90563ef1c1fb1d69273"

json_url = urllib.request.urlopen(url)

data = json.loads(json_url.read())

if (path.isfile('answer.json')): 
    print('Arquivo já existe')
else:
    with open('answer.json', 'w') as outfile: json.dump(data, outfile)
    print('Arquivo gravado')

cifrado = data.get("cifrado").lower()

for letra in cifrado:
    if letra in alfabeto:
        posicao = alfabeto.find(letra)
        posicao = (posicao - casas) % 26
        decifrado = decifrado + alfabeto[posicao]
    else:
        decifrado = decifrado + letra
print (decifrado)

data["decifrado"] = decifrado

print(data)

resumo_criptografico = hashlib.sha1(decifrado.encode('utf-8')).hexdigest()

data["resumo_criptografico"] = resumo_criptografico

print(data)

with open('answer.json', 'w') as outfile: json.dump(data, outfile)

def send():
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=aca1db91a274e399134ef90563ef1c1fb1d69273'
    files = {'answer': open('answer.json', 'rb')}
    r = requests.post(url, files=files)
    r.text
    print(r.status_code)
    print(r.text)

send()





