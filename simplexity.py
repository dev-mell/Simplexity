import numpy as np
from fractions import Fraction as f


'''
Simplexity - escalonamento de matrizes pelo método simplex utilizando python

Programa que resolve problemas de álgebra linear matricial (eslonamento) 
utilizando o método simplex e teorema de gauss-jordan.
Limitações: ele apenas consegue resolver problemas de maximização e 
não de minimização :(
    
Como usar: Adicione os valores do problema no arquivo 'input.txt
após isso, será gerada a solução no arquivo 'output.txt'

*Caso ocorra erro FileNotFoundError, significa que o arquivo está
sendo procurado no ambiente virtual de execução e não na pasta em si
que ele está. Executar pelo terminal -> python3 caminho/do/simplex_v2.py

Autoria: Mell Marinho (@mell.tec)
'''


def output(add, end=None):
    with open('output.txt', 'a') as arq:
        if end != None: 
            print(add, end=end)
            arq.write(add)
        else:
            print(add)
            arq.write(add+'\n')
            
             
def modelagem(matrix):
    with open('output.txt', 'w') as arq:
        output(f'\n{" Modelagem ":=^88}')
        #exibindo a FO
        output(f'Max Z = ', end='')
        for i in range(quant_var):
            aux = str(matrix[-1,i]*-1)
            if i == quant_var-1:output(f'{aux:{len(aux)+1}}x{i+1}')
            else:output(f'{aux:{len(aux)+1}}x{i+1} + ', end='')
        #exibindo as restrições
        for i in range(quant_rest):
            for j in range(quant_var+1):
                if j == quant_var-1:   #se for o penúltimo valor...
                    aux = str(matrix[i,j])
                    output(f'{aux:{len(aux)+1}}x{j+1}', end='')
                elif j == quant_var:   #se for o último valor...
                    aux = str(matrix[i,-1])
                    output(f' <= {aux:{len(aux)+1}}')
                else: 
                    aux = str(matrix[i,j])
                    output(f'{aux:{len(aux)+1}}x{j+1}', end='')
                    output(' + ', end='')
        output('sendo ', end='')
        for i in range(quant_var): output(f'x{i+1} ', end='')
        output('>= 0')
                
           
def row_format(row_index):
    #global quant_rest, quant_var
    for a in range(quant_rest+quant_var+1):
        aux = str(tableau[row_index,a]) #ta bom de transformar em classe isso ai
        output(f'{aux:^8}',end='')
    output('\n')


def tab_format(matrix):
    global quant_rest, quant_var
    output('v'*88)
    output('     ', end='')
    for a in range(quant_rest+quant_var):
        output(f'x{a+1}         ', end='')
    output('R')

    for a in range(quant_rest+1):
        if a == quant_rest:
            output('Z = ', end='')
        for b in range(len(tableau[a])):
            aux = str(matrix[a,b])
            if b == 0 and a == quant_rest:
                output(f' {aux:6}',end='')
            else:output(f'     {aux:6}',end='')
        output('\n   ')
    output('='*88)
    
    
def data_analysis(matrix):
    aux = float(matrix[-1,-1])
    output(f'Portanto,\nZ = {aux:.4f}')
    for i in range(len(basis_var)):
        output(f'{basis_var[i]} = ',end='')
        aux = float(matrix[i,-1])
        output(f'{aux:.4f}')
    
 
array = list()
with open("input.txt", "r") as txt:
    #obtendo num de restricoes e variaveis do doc
    txt_list = txt.readlines()
    quant_var = int(txt_list[2])
    quant_rest = int(txt_list[5])
    
    #criando tableou
    tableau = np.zeros([quant_rest+1, quant_var+quant_rest+1])
    tableau = tableau.astype('int64')
    tableau = tableau + f()

    #obtendo a FO
    fo_txt = txt_list[8]
    fo_txt = fo_txt.split(' ')
    for i in fo_txt: array.append(float(i))
    
    for i in range(len(array)):
        tableau[-1,i] = f(str(array[i]))
        tableau[-1,i] *= -1
        
    #obtendo as restr
    for num in range(quant_rest):
        array.clear()
        rest_txt = txt_list[11+num]
        rest_txt = rest_txt.split(' ')
        for i in rest_txt: array.append(float(i))
            
        for i in range(len(array)):
            if array[i] == array[-1]: tableau[num,-1] = f(str(array[i]))
            else:tableau[num,i] = f(str(array[i]))
        
for a in range(quant_rest): tableau[a,quant_var+a] = f(1)

#output inicial
modelagem(tableau)
#variaveis de base
basis_var = dict()
for val in range(quant_rest): #indice = linha, item = x da coluna
    basis_var[val] = f'x{val+quant_rest}'
#montando tableau
output(f'\n{" Tableau Inicial ":=^88}')
tab_format(tableau)

valid, cont = -1, 1
while valid < 0:
    output(f'---> Iteração {cont}')
    #achando a coluna pivot
    min_col = min(tableau[-1])
    pivot_col_index = tableau[-1].tolist().index(min_col)
    output(f'Coluna pivot: {pivot_col_index+1}ª')
    
    #dividindo os resultados pela coluna pivot
    result_lst = list()
    for i in range(quant_rest): #são só as restrições q se divide e não a FO
        if tableau[i,pivot_col_index] <= 0: 
            result_lst.append(f(0))
        else: 
            result_lst.append(tableau[i,-1]/tableau[i,pivot_col_index])
        
    #definindo a linha pivot
    min_row = sum(result_lst)
    for i in range(len(result_lst)):
        if result_lst[i] > 0 and result_lst[i] < min_row: 
            min_row = result_lst[i]
    pivot_row_index = result_lst.index(min_row)
    output(f'Linha pivot: {pivot_row_index+1}ª')
    
    #variavel que entra e variavel q sai
    basis_var[pivot_row_index] = f'x{pivot_col_index+1}'
    
    #primeira linha - linha pivot
    pivot = tableau[pivot_row_index,pivot_col_index]
    tableau[pivot_row_index] /= pivot
    output(f'Elemento pivotante: {pivot}')
    output(f'\nNova linha pivot: ',end='')
    row_format(pivot_row_index)
    
    #zerando as linhas restantes
    for a in range(quant_rest+1):
        num = str(tableau[a,pivot_col_index]*-1)
        # n usar a linha do pivot e saber se o num na coluna do pivot é zero
        if a != pivot_row_index and tableau[a,pivot_col_index] != 0: 
            tableau[a] += (tableau[pivot_row_index]*tableau[a,pivot_col_index]*-1)
            output(f'Linha {a+1}: (L{pivot_row_index+1} ',end='')
            output(f'x {num}) + L{a+1}')
            output(f'>Nova linha {a+1}: ',end='')
            row_format(a)
        
    tab_format(tableau)

    for i in range(quant_var+quant_rest+1):
        if tableau[-1,i] >= 0: valid = 1
        else:
            valid = -1
            cont += 1
            if cont > quant_rest+1: 
                break
            break
        
data_analysis(tableau)
