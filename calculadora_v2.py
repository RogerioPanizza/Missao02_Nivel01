
# Calculadora v 2.0

saida = ""

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b
    
def multiplicacao(a, b):
    return a * b
    
def divisao(a, b):
    if b == 0:  # Verificação correta de divisão por zero
        return 'Não foi possível realizar a divisão por 0'
    return a / b

# Loop para a execução contínua da calculadora até que o usuário decida sair
while saida.lower() != "n":  # Correção da condição de saída do loop
    # Solicitando ao usuário para inserir os números
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))
    # Solicitando ao usuário para inserir a operação desejada
    operacao = input('Qual o cálculo que deseja fazer? (+, -, *, /): ')
    
    # Verificando a operação e chamando a função correspondente
    if operacao == "+":
        resultado = adicao(num1, num2)
    elif operacao == "-":
        resultado = subtracao(num1, num2)
    elif operacao == "*":
        resultado = multiplicacao(num1, num2)
    elif operacao == "/":
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida'
    
    # Exibindo o resultado da operação
    print('Resultado:', resultado)
    
    # Solicitando ao usuário se deseja sair da calculadora
    saida = input('Deseja sair da calculadora? (S/N): ')    

# Mensagem de fim da execução do programa
print('Fim da execução do programa')
