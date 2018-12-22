import pandas as pd

df = pd.read_csv('python/jupyter_virtual_env/dados.csv', encoding='ISO-8859-1', sep=';')

def pesquisa_binaria(A, item):
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio] == item:
            return meio
        elif A[meio] > item:
            direita = meio - 1
        else: # A[meio] < item
            esquerda = meio + 1 
    return meio if abs(item - A[meio]) < abs(item - A[meio - 1]) else meio -1

nro_requerido = 300
resultado = df['% pontos'].loc[pesquisa_binaria(df['Dif_Ranting'], nro_requerido)]
print(resultado)