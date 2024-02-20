nome = input('Digite seu nome: ')

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))



imc = peso/(altura**2)


print(f'Olá {nome}, seu IMC é {imc:.2f}')