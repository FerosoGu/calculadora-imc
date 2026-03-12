largura = float(input("Qual é a largura do andaime? "))
comprimento = float(input("Qual é o comprimento do andaime? "))
altura = float(input('Qual é a altura do andaime? '))
quanti_andaime = float(input('Quantos andaimes? '))

Guarda_c = input("Possuí Guarda-Corpo? Sim ou Não. ")


if Guarda_c == "Sim":
    l_g_corpo = float(input('Qual é a Largura do Guarda-Corpo? '))
    c_g_corpo = float(input('Qual é o comprimento do Guarda-Corpo? '))
    quant_corpo = float(input("Quantos Guarda-corpo? "))
    guarda_corpo = l_g_corpo*c_g_corpo*quant_corpo

else:
    print('Não possuí Guarda-Corpo')


andaime = largura*comprimento*altura*quanti_andaime
escada = 0.75*0.75*altura*quanti_andaime
forração = (largura-0.2)*(comprimento+0.4)
volume = andaime + escada


valor_montagem = (volume*27.85) + (forração*6.44)


linha_1  = f'O andaime possui {andaime} metros cubico,tamanho da escada {escada}, tamanho da forração {forração}, volume total {volume}'

print(linha_1)
print(valor_montagem)

print("Andaime", andaime)
print("escada", escada)
print('forração', forração)
print("Total", volume)
print()