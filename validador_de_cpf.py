lista3 = []
dados = {}
invalido = int()
valido = int()
print('==========PROGRAMA VALIDADOR DE CPF==========')
resp = input('deseja iniciar o programa: (s/n) \n').upper()
while resp != 'S' and resp !='N':
    resp = input('resposta invalida!! digite uma valor valido: \n').upper()
if resp == 'N':
    print('programa finalizado')
elif resp == 'S':
    print('programa iniciado!!!')
    while True:

        cpf = []
        lista = []
        lista2 = []
        numeros = [10,9,8,7,6,5,4,3,2]
        segundodig = int()
        for i in range(1,12):
            cpf.append(int(input(f'digite o {i}° numero do cpf: \n')))
        cpf2 = cpf[:]
        for i in range(0,2):
            x = cpf.pop(9)
        for i in range(len(numeros)):
            lista.append(cpf[i]*numeros[i])
        soma = sum(lista)

        resto = soma % 11
        if resto < 2:
            primeirodig =0
        else:
            primeirodig = 11 - resto
        cpf.append(primeirodig)
        numeros.insert(0, 11)

        for i in range(len(numeros)):
            lista2.append(cpf[i]*numeros[i])
        soma2 = sum(lista2)

        resto2 = soma2 % 11
        if resto2 < 2:
            sugundodig = 0
        else:
            segundodig = 11 - resto2
        cpf.append(segundodig)

        dados['cpf'] = cpf2

        if cpf != cpf2 or cpf[9] == cpf[10]:
            dados['validacao'] = 'invalido'
            invalido+=1
        else:
            dados['validacao'] = 'valido'
            valido += 1

        lista3.append(dados.copy())

        resp = input('deseja continuar: (s/n) \n').upper()
        while resp != 'S' and resp != 'N':
            resp = input('erro!! digite um valor valido: \n').upper()
        if resp == 'N':
            print('programa finalizado!!')
            break
        else:
            continue
print('resultado dos cpfs testados: \n')
for i in range(len(lista3)):
    print(lista3[i])

total = invalido + valido

print(f'os foram testados:{total}')
print(f'a quantidade de cpfs validos e de: {valido}')
print(f'a quantidade de cpfs invalidos e de: {invalido}')
print(f'a procentagem de cpfs validos e de: {(valido*100)/total}')
print(f'a procentagem de cpfs invalidos e de: {(invalido*100)/total}')
