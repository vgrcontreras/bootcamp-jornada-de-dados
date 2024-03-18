"""
Escreva um programa em python que solicita ao usuário para digitar o seu nome, o valor do seu salário mensal e o valor do bônus
que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário
em comparação com o bônus recebido.
"""

nome = input('Digite o seu nome: ')
salario = float(input(f'{nome}, informe o seu salário: '))
porcentagem_bonus = float(input('Informe também a porcentagem do seu bônus: '))
valor_bonus = 1000 + (salario * porcentagem_bonus)

print(f'Olá {nome}, o seu salário é de {salario} e o seu bônus foi de {valor_bonus - salario}')