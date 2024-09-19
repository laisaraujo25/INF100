# Autor: Carlos Goulart
# Data: 23/08/2024
# Este programa cria um arranjo mxn de numeros inteiros aleatórios no intervalo
# 10 - 30 e exibe uma estatística sobre os números gerados

import p13 as mb     # mb = minha biblioteca
import numpy as np

def main():
    m = n = 8 # define as dimensões do arranjo bidimensional
    valor_min = 10   # menor valor aleatório = 10
    valor_max = 30   # maior valor aleatório = 30
    np.random.seed(1) # inicializa a semente para gerar números aleatórios
    altit = np.random.randint(valor_min, valor_max+1, size=(m, n))

    # imprime o mapa de altitudes
    print('Arranjo original:')
    mb.imprimeMatriz(altit)  # usa a função imprimeMatriz() da biblioteca p13 
    
    # encontra o maior valor usando a função achaMenor
    menor = mb.achaMenor(altit) # usa a função achaMenor() da biblioteca p13
    # exibe a primeira resposta
    print('\nMenor valor encontrado: %d' %menor)

    # encontra o número de vezes que o menor valor aparece usando a função contaMenor
    nmenor = mb.contaMenor(altit, menor) # usa a função contaMenor() da biblioteca p13
    # exibe a segunda resposta
    print('Valor %d foi encontrado %d vezes.' %(menor, nmenor))

# programa principal
main()  # chama a função main() para executar o seu código
