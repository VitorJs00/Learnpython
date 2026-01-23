import base64
import json
import os
import string 
import random
with open('./dados/logo.png','rb') as arquivo:
    arquivo_b64 = base64.b64encode(arquivo.read())

cadastros = [
    {
        "nome":'Joao',
        "idade":31,
        "profissoes":["estagiario","dev python","eng Software"]
    },
    {
        "nome":'Pedro',
        "idade":24,
        "profissoes":["Junior","dev Java","eng alimento"]
    }
]
print(json.dumps(cadastros,ensure_ascii=False))
os.mkdir("./novapasta")

print( os.listdir("./"))
if os.path.exists("./novapasta"):
    os.rename("./novapasta",'renomeada')
print(os.path.getsize('renomeada'))
os.rmdir('renomeada')
senha=''
for _ in range(30):
    senha+=random.choice(string.ascii_letters+string.octdigits)
print(senha)