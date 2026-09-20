import os
import pandas as pd 

lista_arquivos = os.listdir("Curso Básico de Python/Curso Básico de Python/Vendas")
print(lista_arquivos)

tabela_total = pd.DataFrame()

for arquivo in lista_arquivos:
    print(arquivo)
    print(f'Curso Básico de Python/Curso Básico de Python/Vendas/{arquivo}')
    if 'Vendas' in arquivo:
        tabela = pd.read_csv(f'Curso Básico de Python/Curso Básico de Python/Vendas/{arquivo}')
        tabela_total = tabela_total.append(tabela)

print(tabela_total)

