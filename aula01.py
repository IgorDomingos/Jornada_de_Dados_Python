### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

nome = input("Olá! Por favor, digite o seu nome: ")
salario = float(input("Digite o seu salário: "))
valor_bonus = float(input("Informe o valor do bônus: "))

valor = 1000 + salario*valor_bonus
print("******************************")
print(f"Olá, {nome}!! O seu bônus foi de {valor:.2f}")
print("******************************")