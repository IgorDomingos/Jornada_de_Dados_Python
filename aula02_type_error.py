# Exercícios
# Aqui estão cinco exercícios que envolvem TypeError, 
# verificação de tipo (type check), o uso de try-except para tratamento de exceções e a utilização da 
# estrutura condicional if. Esses exercícios aumentam progressivamente em dificuldade e abordam situações
# práticas onde você pode aplicar esses conceitos.

# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao 
# usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando 
# qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
    temperatura = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = (temperatura*(9/5)) + 32 
    print(f"A tempertatura é de {fahrenheit} graus Fahrenheit.")

except ValueError:
    print("valor não é numérico")

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente 
# desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica:
# Utilize a função isinstance() para verificar o tipo da entrada.

entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")



# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário.
# Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar 
# a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

n1 = float(input("Digite um número: "))
operador = input("Digite o operador do cálculo: ")
n2 = float(input("Digite o segundo número"))
resultado = 0
try:
    if operador == '+':
        resultado = n1 + n2
    elif operador == '-':
        resultado = n1 - n2
    elif operador == '*':
        resultado = n1 * n2
    elif operador == '/':
        resultado = n1/n2
    else:
        TypeError
except:
    


# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a 
# entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero".
# Adicionalmente, identifique se o número é "par" ou "ímpar".

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a
# string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e 
# validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um 
# inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista
# de inteiros.