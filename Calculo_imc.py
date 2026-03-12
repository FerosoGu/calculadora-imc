nome = 'Jonas'
altura = 1.69
peso = 84
imc = peso/(altura*2)
print(nome)
print(altura)
print(peso)
print(imc)
if imc < 18.5: #Abaixo de 18,5: Abaixo do peso
    print('Abaixo do peso')
elif 18.6 >= imc < 24.9: #18,5 - 24,9: Peso normal
    print('Peso normal')
elif 25.0 >= imc <29.9: #25,0 - 29,9: Sobrepeso
    print('sobre peso')
elif 30.0 >= imc <= 39.9: #30,0 - 39,9: Obesidade
    print('Obesidade')
elif imc >= 40.0:#40,0 ou mais: Obesidade grave
    print('Obesidade grave')
 








