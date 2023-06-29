import sys

# Lista 1 - Aula 4
# 1. Desenvolva um programa que leia dois números e informe o maior deles.
def ex1():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    if num1 > num2:
        print(num1, " é o maior número.")
    else:
        print(num2, " é o maior número.")

# 2. Faça um código que leia um número informado pelo usuário e que ao final informe se o número é par ou ímpar.
def ex2():
    numero = int(input("Digite um número: "))
    tipo = numero%2
    if tipo == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

# 3. Partindo da solução da questão anterior. Crie um programa que calcule o quadrado de um número quando ele for par e que calcule o cubo do número caso ele seja ímpar.
def ex3():
    numero = int(input("Digite um número: "))
    tipo = numero%2
    if tipo == 0:
        print(f"O quadrado de {numero} é {numero**2}.")
    else:
        print(f"O cubo de {numero} é {numero**3}.")

# 4. Faça um programa que receba 3 notas de prova de um aluno, calcule a média e diga se ele foi aprovado ou reprovado. A média para aprovação é de pelo menos 6 (aprovado se média maior ou igual a 6).
def ex4():
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    n3 = float(input("Digite a nota 3: "))
    media = (n1+n2+n3)/3
    if media < 6:
        print(f"Sua nota foi {media}. Você está reprovado.")
    else:
        print(f"Sua nota foi {media}. Você está aprovado.")

# 5. Escreva um programa que leia dois números e que pergunte qual operação o usuário deseja realizar. Esse programa deve aceitar como respostas a soma(+), a subtração(-), a multiplicação (*) e a divisão (/). Ao final, o programa deve exibir o resultado da operação escolhida.
def ex5():
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    operacao = input("Agora, digite a operação a ser realizada.\n(+) para soma\n(-) Para subtração\n(*) Para multiplicação\n(/) Para divisão")
    if operacao == "+":
        print(f"{n1} + {n2} = {n1+n2}")
    elif operacao == "-":
        print(f"{n1} - {n2} = {n1-n2}")
    elif operacao == "*":
        print(f"{n1} * {n2} = {n1*n2}")
    elif operacao == "/":
        print(f"{n1} / {n2} = {n1/n2}")
    else:
        print("Operação inválida.")

# 6. Escreva um programa que pergunte a distância que determinado passageiro deseja percorrer em km. A partir disso calcule o preço da passagem. É cobrado 0,50 centavos por km para viagens de até 300 km. E 0,45 centavos para viagens mais longas.
def ex6():
    distancia = float(input("Digite a distância da sua viagem: "))
    if distancia < 300:
        valor = "{:.2f}".format(distancia * 0.50)
    else:
        valor = "{:.2f}".format(distancia * 0.45)
    
    print(f"O valor da passagem será de R$ {valor.replace('.', ',')}.")

# 7. Suponha que determinado usuário possua 2 logins em uma rede corporativa.
# Login 1
# usuario: jardim
# senha: flores1206
# Login 2
# usuario: cordeiro
# senha la1506
# Escreva um programa que valide o acesso do usuário na rede. Caso o par usuário e senha estejam corretos, o programa deve imprimir a mensagem: "Seja bem vindo!". Caso contrário, "Usuário e senha não conferem".
def ex7():
    u1 = "jardim"
    s1 = "flores1206"
    u2 = "cordeiro"
    s2 = "la1506"
    usuario = input("Digite o nome de usuário: ")
    if usuario == u1:
        senha = input("Digite a senha: ")
        if senha == s1:
            print("Login realizado com sucesso.")
        else:
            print("Falha no login.")
    elif usuario == u2:
        senha = input("Digite a senha: ")
        if senha == s2:
            print("Login realizado com sucesso.")
        else:
            print("Falha no login.")
    else:
        print("Usuário inválido.")

# 8. Uma empresa concederá aumento de salário aos seus funcionários de acordo com o cargo.
# Cargo - Aumento(%)
# Gerente Geral - 30
# Gerente de Relacionamento - 30
# Analista - 25
# Assistente de Atendimento - 20
# Crie um programa que solicite o salário e o cargo do funcionário. O programa deve calcular e imprimir o novo salário. Caso o cargo informado não esteja na tabela, o programa deve imprimir "Cargo inválido".

# executar o exercício
if __name__ == "__main__":
    if len(sys.argv) > 1:
        function_name = sys.argv[1].replace("-", "")  # Remover o sinal "-"
        function = locals().get(function_name)
        if function:
            function()
        else:
            print("Função não encontrada.")
    else:
        print("Nenhuma função especificada.")