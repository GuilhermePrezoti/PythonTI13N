import this
this.contador = 0
this.num = 0
this.soma = 0
this.a = 0
this.maior = 0
this.num1 = 0
this.menor = 0

def exercicio01():
    A = 10
    B = 20
    msg = 'Antes da troca: A = {}, B = {}'. format(A,B)
    aux = A
    A = B
    B = aux
    msg = msg + '\nDepois da Troca: A = {}, B = {}'. format(A,B)
    return msg

def exercicio02():
    A = int(input('Digite o número que você deseja: '))
    B = A -1
    print ('O seu número A {}, e o seu antecessor é B = {}'. format(A,B))

def exercicio03():

    bas = float(input('Digite a Base: '))
    alt = float(input('Digite a Altura: '))
    c = bas*alt
    return print('O Resultado é de : c {} '. format (c))

def exercicio04():
    idade = int(input('Qual sua idade? '))
    ano = 365
    mes = 30
    A = idade * ano + mes

    print ('O tatal vidas que você tem é de A {} '. format(A))

def exercicio05():
    votos = int(input('Quantos votos teve no municipio? '))
    white = int(input('Quantos votos Brancos? '))
    nulos = int(input('Quantos votos Nulos? '))
    validos = int(input('Quantos vatos invalidos? '))
    d = 100
    A = (votos/white) * d
    B = (votos/nulos) * d
    C = (votos/validos) * d


    print ('A porcentagem dos votos Branco é de white: {} ' . format (A))
    print ('A porcentagem dos votos Branco é de nulos: {} ' . format (B))
    print ('A porcentagem dos votos Branco é de validos: {} ' . format (C))

def exercicio06():
    salario = float(input('Qual é o seu salário? '))
    perc = float(input('Qual a porcentagem que você quer adicionar? '))
    A = salario + (salario * perc / 100)
    print ('Seu novo salario é de A = {}  '. format (A))

def exercicio07():
    fabrica = float(input('Qual valor do carro? '))
    novoValor = (fabrica + fabrica * 0.45 + fabrica * 0.28)
    print ('O novo valor do carro é de novoValor = {}'. format (novoValor))

def exercicio08():
    nota1 = float(input('Qual a primeira nota?' ))
    nota2 = float(input('Qual a segunda nota? '))
    nota3 = float(input('Qual a terceira nota? '))
    notaFinal = (nota1 + nota2 + nota3 / 10)
    print ('A nota total do aluno foi de notaFinal = {} '. format (notaFinal))

def exercicio09():

    maca = 1.30
    maca2 = 1.00

    question = int(input(('Qual a quantidade de maças você quer comprar? ')))

    if maca > 11:
        maca * 1
        print ('A Maça custa maca = {}' . format(maca))
    else: maca2 < 12
    maca2 * 1
    print ('A Maça custa maca2 = {} ' . format(maca2))

def exercicio10():
    for numero in range(0,11):
        print('Os némeros na ordem crescentes são numero = {} '.format (numero))

def exercicio11():
    salario = float(input('Qual seu salario? '))
    vendas = int(input('Qal o total de vendas? '))
    comi = 0.3
    ultra = 0.5
    novoSalario = salario + (salario / vendas * 3 * 5 )
    print ('Seu novoSalario = {} ' . format(novoSalario))

def exercicio12():
    saldo = float(input('Qual seu saldo? '))
    debito = float(input('Quantos reais você possui no débito? '))
    credito = float(input('Quantos reais no crédito você possui? '))
    saldoAtual = (saldo - debito + credito)
    print('Seu saldoAtual = {}' . format (saldoAtual))
    if saldoAtual >= 0:
        print ('Saldo Possitvo!')
    else:
        print('Saldo Negativo!')

def exercicio13():

    num = int(input('Qual numero você deseja? '))
    print (' {} * {} = {} ' . format(num, 1, num * 1))
    print (' {} * {} = {} '.format(num, 2, num * 2))
    print(' {} * {} = {} '.format(num, 3, num * 3))
    print(' {} * {} = {} '.format(num, 4, num * 4))
    print(' {} * {} = {} '.format(num, 5, num * 5))
    print(' {} * {} = {} '.format(num, 6, num * 6))
    print(' {} * {} = {} '.format(num, 7, num * 7))
    print(' {} * {} = {} '.format(num, 8, num * 8))
    print(' {} * {} = {} '.format(num, 9, num * 9))
    print(' {} * {} = {} '.format(num, 10, num * 10))

def exercicio14():
    N = int(input('Informe um número: '))
    if N > 0:
     for i in range (N+1):
      print ('O números são N = {}' . format(N))
#Exercicio Errado...

def exercicio15():
    for i in range(10):
        print('Informe um número: ')
        num = int(input())
        if num < 0:
            this.contador = this.contador + 1
            print('A quantidade de números negativos é = {}'.format(this.contador))

def exercicio16():
    for i in range(10):
        print('Informe os números: ')
        this.num = int(input())

        if this.num < 40:
            this.soma = this.soma + this.num
            print('A soma dos número foi de = {}'. format(this.soma))

def exercicio17():
    a = 14
    b = 100
    total = (a + b) / 2
    print('As médias do números é de = {}'. format(total))

def exercicio18():
    this.maior = vet [0]
    this.menor = vet [0]

    for i in range(10):
        if vet [0] > this.maior:
            this.maior = vet[0]

            if vet[0] < menor:
                menor < vet[0]
   print('O maior número digitado foi = {} '.format(this.maior))






