print(not True)
print(not False)

senha = input("digite a senha:")
print(bool(senha))
if not senha:
    print('nao digitou')
elif senha=="123":
    print('logado')
else:
    print('error')