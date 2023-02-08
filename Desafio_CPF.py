cpf = input('Por favor, digite um CPF para validação (no formato XXX.XXX.XXX-XX): ')

for caractere in cpf:
    if caractere == '.':
        cpf = cpf.replace('.','')
    elif caractere == '-':
        cpf = cpf.replace('-','')
    else:
        cpf = cpf

lista_numeros_cpf = list(cpf)
contador = 10
validacao_etapa_1 = 0
validacao_etapa_2 = 0
digito_1=0

for i in lista_numeros_cpf[0:9]:
    validacao_etapa_1 += (int(i) * contador)
    contador -= 1

validacao_digito_1 = (11 - (validacao_etapa_1 % 11))

if validacao_digito_1 > 9:
    digito_1 = 0
elif validacao_digito_1 <= 9:
    digito_1 = validacao_digito_1

print(f'O primeiro dígito após o hífen deve ser: {digito_1}')

contador = 11
lista_numeros_cpf.insert(10, digito_1)

for i in lista_numeros_cpf[0:10]:
    validacao_etapa_2 += (int(i) * contador)
    contador -= 1

validacao_digito_2 = 11 - (validacao_etapa_2 % 11)

if validacao_digito_2 > 9:
    digito_2 = 0
elif validacao_digito_2 <= 9:
    digito_2 = validacao_digito_2

print(f'O segundo dígito após o hífen deve ser: {digito_2}')

lista_numeros_cpf.insert(11, digito_2)

if lista_numeros_cpf[0] == lista_numeros_cpf [1] and lista_numeros_cpf [1] == lista_numeros_cpf [2] and \
    lista_numeros_cpf[2] == lista_numeros_cpf [3] and lista_numeros_cpf [3] == lista_numeros_cpf[4] and \
    lista_numeros_cpf[4] == lista_numeros_cpf[5] and lista_numeros_cpf[5] == lista_numeros_cpf[6] and \
    lista_numeros_cpf[6] == lista_numeros_cpf[7] and lista_numeros_cpf[7] ==lista_numeros_cpf[8] and \
    lista_numeros_cpf[8] == lista_numeros_cpf[9]:
    print('CPF inválido.')
elif int(lista_numeros_cpf[9]) == int(lista_numeros_cpf[10]) and int(lista_numeros_cpf[11]) == int(lista_numeros_cpf [12]):
    print('CPF válido.')
else:
    print('CPF inválido.')
