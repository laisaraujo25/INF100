# Nome: Laís Pedrosa Araújo
# Data: 20/08/2024
# Comentário: O programa cria uma imagem, a rotaciona e altera a cor de uma porção dela

# o arquivo imagens.py deve estar no mesmo diretório do programa
import imagens
# o arquivo coresT com a figura deve estar no mesmo diretório deste arquivo 
imagem1 = imagens.Imagem('coresT.jpg')
imagem1.mostrar()   # Mostrar a imagem1 na tela
lin1 = imagem1.altura  # descobre o número de linhas da imagem1
col1 = imagem1.largura # descobre o número de colunas da imagem1
print('A imagem tem %d linhas e %d colunas.' %(lin1, col1))

###### escreva o seu código abaixo desta linha #####

imagem2 = imagens.Imagem('', (col1, lin1))
for i in range(0, col1): 
    for j in range(0, lin1): 
        imagem2[i][j] = imagem1[j][i]
imagem2.mostrar()

imagem3 = imagens.Imagem('', (col1, lin1))
for i in range(0, col1):
    for j in range(0,lin1):
        imagem3[i][j] = imagem2[i][j]
        if i < (col1//2) and j > (lin1//2):
                r,g,b = imagem3[i][j]
                if r > 100:
                    r = max(0, r-200)
                    imagem3[i][j] = (r, g, b)
imagem3.mostrar()


