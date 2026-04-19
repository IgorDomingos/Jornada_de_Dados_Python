# #Exercício 1: Verificação de Qualidade de Dados 
# Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade 
# e preço. Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso 
# contrário. 
# quantidade = int(input("Digite a quantidade: ")) 
# preco = float(input("Digite o preço: ")) 
 
# if (quantidade > 0 and preco > 0): 
#     print("Dados válidos!") 
# else: 
#     print("Dados inválidos!") 
 
# Exercício 2: Classificação de Dados de Sensor 
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada  
# leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que: 
 
# Temperatura < 18°C é 'Baixa' 
# Temperatura >= 18°C e <= 26°C é 'Normal' 
# Temperatura > 26°C é 'Alta' 
 
# temperatura = int(input("Qual a temperatura? ")) 
 
# if (temperatura < 18): 
#     print("A temperatura está baixa.") 
# elif (18 <= temperatura <= 26): 
#     print("A temperatura está normal.") 
# elif (temperatura > 26): 
#     print("A temperatura está alta.") 
 
# Exercício 3: Filtragem de Logs por Severidade 
# Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. Dado um registro de log em formato de  
# dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, escreva um programa que  
# imprima a mensagem se a severidade for 'ERROR'. 
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'} 
 
# if log['level'] == "ERROR": 
# 	print(log['message']) 
 
# Exercício 4: Validação de Dados de Entrada 
# Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos 
# e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico 
# encontrado. 
 
# idade = 25  # Exemplo de valor, substitua com input do usuário se necessário 
# email = "usuario@exemplo.com"  # Exemplo de valor, substitua com input do usuário se necessário 
 
# idade = int(input("Digite a sua idade: ")) 
# email = input("Digite o seu e-mail: ") 
 
# if not 18 <= idade <= 65: 
#     print("Idade fora do intervalo permitido") 
# elif "@" not in email or "." not in email: 
#     print("Email inválido") 
# else: 
#     print("Dados de usuário válidos") 
 
# Exercício 5: Detecção de Anomalias em Dados de Transações 
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. Uma transação é considerada 
# suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h).  
# Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita. 
# transacao = {'valor': 8000, 'hora': 14} 
 
# if (transacao['valor'] > 10000 or not(9 <= transacao['hora'] <= 18)): 
#     print("Transação suspeita!!") 
# else: 
#     print("Transação normal.") 
 
 
 
#EXERCÍCIOS COM FOR: 
 
 
# 6. Contagem de Palavras em Textos 
# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele. 
# texto = "hoje foi nossa segunda aula do bootcamp , bootcamp de python" 
# palavras = texto.split() 
# contagem = {} 
 
# for p in palavras: 
#     if p in contagem: 
#     	contagem[p] += 1 
#     else: 
#     	contagem[p] = 1 
# print(contagem) 
 
 
# 7. Normalização de Dados 
# Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1. 
 
 
# 8. Filtragem de Dados Faltantes 
# Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando. 
# usuarios = [ 
#     {"nome": "Alice", "email": "alice@example.com"}, 
#     {"nome": "Bob", "email": ""}, 
#     {"nome": "Carol", "email": "carol@example.com"} 
# ] 
 
# usuarios_validos = [usuario for usuario in usuarios if usuario["email"]] 
 
# print(usuarios_validos) 
     
 
# 9. Extração de Subconjuntos de Dados 
# Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares. 
# lista = [4, 5, 17, 7, 8, 47, 6, 9, 10, 63, 78] 
# pares = [] 
# for l in lista: 
#     if l%2 == 0: 
#         pares.append(l) 
 
# print(pares) 
         
# 10. Agregação de Dados por Categoria 
# Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria. 
vendas = [ 
	{"categoria": "eletrônicos", "valor": 1200}, 
	{"categoria": "livros", "valor": 200}, 
	{"categoria": "eletrônicos", "valor": 800} 
] 
 
vendas_por_categoria = {} 
 
for v in vendas: 
    categoria = v["categoria"] 
    valor = v["valor"] 
    if categoria in vendas_por_categoria: 
        vendas_por_categoria[categoria] += valor 
    else: 
        vendas_por_categoria[categoria] = valor 
print(vendas_por_categoria) 
 
# Exercícios WHILE:  
# 11. Leitura de Dados até Flag 
# Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida. 
 
# dados = [] 
# entrada = "" 
# while entrada.lower() != "sair": 
# 	entrada = input("Digite um valor (ou 'sair' para terminar): ") 
#     if entrada.lower() != "sair": 
#         dados.append(entrada) 
 
 
# 12. Validação de Entrada 
# Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida. 
# numero = int(input("Digite um número entre 1 e 10: ")) 
# while numero < 1 or numero > 10: 
#     print("Número fora do intervalo!") 
#     numero = int(input("Por favor, digite um número entre 1 e 10: ")) 
 
# print("Número válido!") 
 
# 13. Consumo de API Simulado 
# Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas. 
 
 
# 14. Tentativas de Conexão 
# Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas. 
 
 
# 15. Processamento de Dados com Condição de Parada 
# Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada. 
 
 
 
 
# DESAFIO:  
# Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas 
try: 
    nome = input("Digite seu nome: ") 
 
    # Verifica se o nome está vazio 
    if len(nome) == 0: 
        raise ValueError("O nome não pode estar vazio.") 
    # Verifica se há números no nome 
    elif any(char.isdigit() for char in nome): 
        raise ValueError("O nome não deve conter números.") 
    else: 
        print("Nome válido:", nome) 
except ValueError as e: 
    print(e) 
 
# Solicita ao usuário que digite o valor do seu salário e converte para float 
 
try: 
    salario = float(input("Digite o valor do seu salário: ")) 
    if salario < 0: 
        print("Por favor, digite um valor positivo para o salário.") 
except ValueError: 
    print("Entrada inválida para o salário. Por favor, digite um número.") 
 
# Solicita ao usuário que digite o valor do bônus recebido e converte para float 
try: 
    bonus_recebido = float(input("Digite o valor do bônus recebido: ")) 
    if bonus_recebido < 0: 
        print("Por favor, digite um valor positivo para o bônus.") 
except ValueError: 
    print("Entrada inválida para o bônus. Por favor, digite um número.") 
 
# Assumindo uma lógica de cálculo para o bônus final e KPI 
bonus_final = bonus_recebido * 1.2  # Exemplo, ajuste conforme necessário 
kpi = (salario + bonus_final) / 1000  # Exemplo simples de KPI 
 
# Imprime as informações para o usuário 
print("*********************************************************************") 
print(f"Seu KPI é: {kpi:.2f}") 
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.") 
print("*********************************************************************") 