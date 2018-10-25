version = 'Xavier'
print(f'''Bem vindo(a) ao {version}. O que deseja calcular:
      Areas
      Volumes
      Funcoes e Equacoes (FE)
      Potencias
      Radicais
      Trigonometria
      Geometria
      Logica Bivalente (LB)
      Vetores
      Estatistica
      Sucessoes
      Derivadas
      Conjuntos e Probabilidades (CB)
      Logaritimos
      Limites Notaveis (LN)
      Numeros Complexos (NC)''')

while True:    
    resposta = input('>>> ').upper()
    if resposta == 'AREAS':
        print('''Qual area deseja calcular:
      Quadrado
      Retangulo
      Triangulo
      Losangulo
      Trapezio
      Poligono Regular
      Circulo
      Cone
      Esfera
      Sair''')
        while True:
            resposta2 = input('> ').upper()
            if resposta2 == 'QUADRADO':
                n1 = int(input('Digite a medida de um dos lados do quadrado: '))
                r = print(f'A area do {resposta2} é: {n1*n1}')
                continue

            elif resposta2 == 'RETANGULO':
                n1 = int(input('Digite o comprimento do retangulo:'))
                n2 = int(input('Digite a largura do retangulo: '))
                r = print(f'A area do {resposta2} é: {n1}*{n2}={n1*n2}')
                continue

            elif resposta2 == 'SAIR':
                break    
            
    else:
        print('erro')
