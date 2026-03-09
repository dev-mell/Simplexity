import numpy as np
from fractions import Fraction as f

#input da ordem da matriz
row_len = int(input('Quantidade de linhas: '))
col_len = int(input('Quantidade de colunas: '))

#'declarando' a matriz
matrix = np.zeros([row_len, col_len])
matrix = matrix.astype('int64') #alterando o tipo de inteiro do numpy
matrix = matrix + f() #modificando as operações para o modo de fração

#input dos numeros
for a in range(row_len):
    for b in range(col_len):
        aux = input(f'a{a+1}{b+1}: ') #float ou int?
        matrix[a,b] = f(aux) #preferi usar uma variável auxiliar para visualizar melhor

print(matrix, '\n')
#resolver por coluna - resolução de uma coluna
for j in range(col_len-1): 
    matrix[j] /= matrix[j,j] #pivot
    print(matrix, '\n')
    
    for i in range(row_len): #igualando cada numero a zero
        if i != j:
            matrix[j] *= matrix[i,j]
            print(matrix,'\n')
            matrix[i] -= matrix[j]
            print(matrix, '\n')
            matrix[j] /= matrix[j,j]
            print(matrix, '\n')

print(matrix)