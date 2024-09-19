# Nome: Laís Pedrosa Araújo
# Matrícula: 117160
# Data: 27/08/2024
# Comentário: O programa cria um arranjo, encontra o menor valor e
# conta quantas vezes ele aparece.

import numpy as np

# Imprime um arranjo bidimensional no formato de linhas e colunas
# Parâmetro de entrada: A - um arranjo bidimensional
# Retorna: não retorna valor 
def imprimeMatriz(A):
    lin, col = np.shape(A) # lin = número de colunas de A e col = número de colunas de A
    for i in range (0, lin):      # i de 0..lin usado como índice de linha
        for j in range (0, col) : # j de 0..col usado como índice de coluna
            print('%5d' %A[i][j], end='') # imprime o elemento da posição (i, j) com maior
        print() # pula para a linha seguinte
    return      # esta função NÂO retorna valor

# Encontra o menor valor em um arranjo bidimensional
# Parâmetro de entrada: A - um arranjo bidimensional
# Retorna: o valor do menor elemento
def achaMenor(A) :
    lin, col = np.shape(A) # lin = número de colunas de A e col = número de colunas de A
    menor = A[0][0]
    for i in range (0, lin):      # i de 0..lin usado como índice de linha
        for j in range (0, col) : # j de 0..col usado como índice de coluna
            if A[i][j] < menor :  # compara o elemento da posição (i, j) com menor
                menor = A[i][j]   # atualiza o menor
    return menor     # retorna o menor elemento de uma matriz A


# implemente abaixo a função solicitada no seu roteiro
# DICA: use a função shape para descobrir o número de linhas e de colunas
# do arranjo a ser precorrido - vide linhas 12 e 23

def contaMenor ( altit, menor ):
    lin, col = np.shape( altit )
    menor = achaMenor( altit )
    nmenor = 0
    for i in range (0, lin):      
        for j in range (0, col):
            if altit[i][j] == menor:
                nmenor = nmenor + 1
    return nmenor

