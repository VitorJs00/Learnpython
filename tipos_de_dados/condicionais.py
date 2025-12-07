n1 = input('numero =')
n2 = input('numero =')
escolha = input('A:para somar, B:para subitrair').upper()


if escolha == "A":
    print(int(n1)+int(n2))
elif escolha == "B":
    print(int(n1)-int(n2))
else:
    print("aa")
