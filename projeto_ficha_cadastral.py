print("Cadastro de doadores de sangue")
nome = input("Por favor, informe seu nome completo: ")
peso = float(input("Por favor, informe o seu peso em kg: "))
altura = int(input("Por favor, informe sua altura em cm: "))
ano_nascimento = int(input("Por favor, me informa seu ano de nascimento: "))

import datetime
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento
peso_minimo = peso > 50
idade_minima = idade >= 16
if peso_minimo and idade_minima:
    print("Pode doar sangue")
else:
    print("Não pode doar sangue")

texto_saida = f"\tNOME: {nome}\n\tPESO: {peso} kg\n\tALTURA: {altura} cm \n\tIDADE: {idade}\n\tTEM PESO MINIMO PARA DOAR: {peso_minimo}\n\tTEM IDADE MINIMA PARA DOAR: {idade_minima}"

print(texto_saida)