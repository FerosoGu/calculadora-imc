Andaime_L = float(input("Qual é a Largura do Andaime? "))
Andaime_C = float(input('Qaul é o comprimento do Andaime? '))
Andaime_A = float(input('Qual é o comprimento do Andaime? '))
Andaime_Quantidade = float(input('Quantos Andaimes? '))


# Forração do Andaime
Forração_Convencional = input('Forração Convencional? "Sim" ou "Não' )
Forração_quantidade = float(input('Quantidade de forração?' ))

if Forração_Convencional == "Sim":
    Forração = ((Andaime_L-0.20)*(Andaime_C+0.40)*Forração_quantidade)
elif Forração_Convencional == "Não":
    Forração_L = float(input("Qual é a largura do forração? "))
    Forração_C = float(input("Qual é o comprimeto da forração? "))
    Forração_Não = Forração_L*Forração_C*Forração_quantidade


# Escada do Andaime
Escada_Convencional = input("Escada convenciona? 'Sim' ou 'Não'")

if Escada_Convencional == 'Sim':
    Escada = (0.75*0.75*Andaime_A)
elif Escada_Convencional == 'Não':
    Escada_L = float(input('Qual é a largura da escada? '))
    Escada_C = float(input('Qual é o comprimento da escada? '))
    Escada_A = float(input('Qual é a altura da escada? '))
    Escada_Não = Escada_L*Escada_C*Escada_A

# Guarda Corpo do Andaime
Tem_GC = input('Possuí Guarda corpo? "Sim" ou "Não" ')

if Tem_GC == "Sim":
    Guarda_Corpo_L = float(input('Qual é o comprimento do Guarda Corpo? '))
    Guarda_Corpo_C = float(input('Qual é o comprimento do Guada corpo? '))
    Guarda_Corpo_Quantidade = float(input('Quantos Guarda Corpo? '))
    Guarda_Corpo = (Guarda_Corpo_L*Guarda_Corpo_C*Guarda_Corpo_Quantidade)
elif Tem_GC == "Não":
    print('Não possuí Guarda Corpo.')

# Resultado do Andaime
Andaime_volulme = (Andaime_L*Andaime_C*Andaime_A*Andaime_Quantidade+Escada)
Andaime_volume_Escada = (Andaime_L*Andaime_C*Andaime_A+Escada_Não)


if Forração_Convencional == "Sim":
    print(f'''
      O Andaime possuí {Andaime_volulme} Metros Cubicos, 
      tamanho da escada {Escada}, 
      Tamanho da forração {Forração_Convencional}
      ''')
elif Forração_Não == "Sim":
    print(f'''
      O Andaime possuí {Andaime_volulme} Metros Cubicos, 
      tamanho da escada {Escada}, 
      Tamanho da forração {Forração_Não}
      ''')
elif Escada_Convencional == "Sim" and Forração_Convencional:
    print(f'''
      O Andaime possuí {Andaime_volulme} Metros Cubicos, 
      tamanho da escada {Escada}, 
      Tamanho da forração {Forração_Convencional}
      ''')
elif Escada_Não == 'Sim' and Forração_Não:
    print(f'''
      O Andaime possuí {Andaime_volume_Escada} Metros Cubicos, 
      tamanho da escada {Escada_Não}, 
      Tamanho da forração {Forração_Não}
      ''')


if Tem_GC == "Sim":
    print(f'Possuí Guarda Corpo {Guarda_Corpo}')





