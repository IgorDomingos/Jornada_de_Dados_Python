# Exercícios: 
# Inteiros (int) 
# 1) Escreva um programa que soma dois números inteiros inseridos pelo usuário. 
 
# n1 = int(input("Digite um número inteiro: ")) 
# n2 = int(input("Digite mais um número inteiro: ")) 
# soma = n1 + n2 
 
# print(f"A soma dos dois números é igual a: {soma}") 
 
# 2) Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5. 
 
# n = int(input("Digite um número: ")) 
# resto_divisao = n%5 
# print(f"O resto da divisão do número {n} por 5 é igual a: {resto_divisao}") 
 
# 3) Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado. 
# nx = int(input("Digite um número inteiro: ")) 
# nx2 = int(input("Digite mais um número inteiro: ")) 
 
# multiplicacao = nx*nx2 
# print(f"O resultado da multiplicação é: {multiplicacao}") 
# 4) Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo. 
 
# nd = int(input("Digite um número inteiro: ")) 
# ndx = int(input("Digite mais um número inteiro: ")) 
# divisao = nd/ndx 
# print(f"A divisão desses dois números é igual a: {divisao}") 
 
# 5) Escreva um programa que calcule o quadrado de um número fornecido pelo usuário. 
# nq = int(input("Digite um número inteiro: ")) 
# quadrado = nq**2 
# print(f"O quadrado de {nq} é: {quadrado}") 
 
# Números de Ponto Flutuante (float) 
# 6) Escreva um programa que receba dois números flutuantes e realize sua adição. 
# nf = float(input("Digite um número flutuante: ")) 
# nfx = float(input("Digite mais um número: ")) 
# adição = nf + nfx 
# print(f"A adição de {nfx} a {nf} resulta em: {adição}") 
 
# 7) Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário. 
 
# nfm = float(input("Digite um número flutuante: ")) 
# nfm2 = float(input("Digite mais um número")) 
# media = nfm+nfm2/2 
# print(f"A média entre {nfm} e {nfm2} é: {media:.2f}") 
 
# 8) Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário). 
# print("Vamos fazer um cálculo de potenciação!") 
# base = float(input("Digite um número para ser a BASE: ")) 
# expoente = float(input("Digite um número para ser o EXPOENTE: ")) 
# potencia = base**expoente 
# print(f"{base} elevado a {expoente} é igual a: {potencia:.2f}") 
 
# 9) Faça um programa que converta a temperatura de Celsius para Fahrenheit. 
# celsius = float(input("Qual a temperatura em graus celsius? ")) 
# fahrenheit = (celsius*(9/5)) + 32 
# print(f"Isso equivale a aproximadamente {fahrenheit} graus Fahrenheit") 
 
# 10) Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada. 
# raio = float(input("Me informe a medida do raio do círculo: ")) 
# area_circulo = 3.14159*(raio**2) 
# print(f"A área do círculo é igual a aproximadamente: {area_circulo:.2f}") 
 
# Strings (str) 
# 11) Escreva um programa que receba uma string do usuário e a converta para maiúsculas. 
# string = input("Digite qualquer coisa: ") 
# string = string.upper() 
# print(string) 
 
# 12) Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas. 
# nome_completo = input("Digite o seu nome completo: ") 
# nome_completo = nome_completo.upper() 
# print(nome_completo) 
 
# 13) Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final. 
 
 
# 14) Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente. 
# data = input("Digite uma data no formato: dd/mm/aaaa ") 
# dts = data.split("/") 
# print(f"Dia: {dts[0]}") 
# print(f"Mês: {dts[1]}") 
# print(f"Ano: {dts[2]}") 
 
# 15) Escreva um programa que concatene duas strings fornecidas pelo usuário. 
# s1 = input("Escreva uma string: ") 
# s2 = input("Escreva outra string: ") 
# s_ = s1+s2 
# print(s_) 
 
# Booleanos (bool) 
# 16) Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas. 
# bo1 = True 
# bo2 = False 
# print(f"A operação booleana 'AND' entre {bo1} e {bo2} é igual a: {bo1 and bo2}") 
 
# 17) Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR. 
# bor1 = True 
# bor2 = False 
# print(f"A operação booleana 'OR' entre {bor1} e {bor2} é igual a: {bor1 or bor2}") 
 
# 18) Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor. 
# valor = bool(input("digite um valor booleano: ")) 
# valor = not valor 
# print(valor) 
 
# 19) Faça um programa que compare se dois números fornecidos pelo usuário são iguais. 
# numero_1 = int(input("Digite um número: ")) 
# numero_2 = int(input("Digite outro número: ")) 
# if (numero_1 == numero_2): 
#     print("Os números são iguais") 
# else: 
#     print("Os números são diferentes") 
 
# 20) Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes. 
numero_1 = int(input("Digite um número: ")) 
numero_2 = int(input("Digite outro número: ")) 
if (numero_1 != numero_2): 
    print("Os números são diferentes") 
else: 
    print("Os números são iguais")
