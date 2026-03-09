# Simplexity - Simplex Method Solver

Implementação do **Método Simplex** em Python para resolução de problemas de programação linear com maximização de função objetivo.

---

## Sobre

Este projeto resolve problemas de **Programação Linear (PL)** utilizando o Método Simplex. A partir de um arquivo de entrada com a função objetivo e as restrições do problema, o algoritmo:

- Exibe a **modelagem** do problema (função objetivo + restrições)
- Monta o **tableau inicial** com as variáveis de folga
- Executa as **iterações do pivoteamento** passo a passo, exibindo cada operação realizada
- Apresenta a **solução ótima** com os valores de Z e das variáveis de decisão

Todas as saídas são exibidas no terminal e salvas automaticamente em `output.txt`, com os cálculos feitos com precisão exata via frações racionais (`Fraction`).

---

## Requisitos

- Python **3.8+**
- Biblioteca [NumPy](https://numpy.org/)
- Ter conhecimento sobre o método simplex

---

## Como usar

### 1. Configure o arquivo de entrada

Crie um arquivo `input.txt` na mesma pasta do script, seguindo **exatamente** o formato no arquivo modelo `input.txt`.

**Exemplo** — problema com 2 variáveis e 2 restrições:

```
Num de variaveis:

2

Num de restricoes:

2

FO (Max Z):

5 4

Restricoes (<=):

6 4 24
1 2 6
```

Neste exemplo, o problema modelado é:

```
Max Z = 5x1 + 4x2
s.a.:
  6x1 + 4x2 <= 24
   x1 + 2x2 <= 6
  x1, x2 >= 0
```

### 2. Execute o script

```bash
python simplexity.py
```

### 3. Leia os resultados

A solução será exibida no terminal e gravada em `output.txt`. A saída inclui:

- A modelagem completa do problema
- O tableau a cada iteração com as operações de linha realizadas
- O valor ótimo de **Z** e de cada variável de decisão


Autora: Mell Marinho (@mell.tec)
