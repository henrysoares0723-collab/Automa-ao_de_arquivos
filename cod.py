import os
import pandas as pd 


lista_arquivos = os.listdir("Curso Básico de Python/Curso Básico de Python/Vendas")

tabela_total = pd.DataFrame()
for arquivo in lista_arquivos:
    if 'Vendas' in arquivo:
        tabela = pd.read_csv(f'Curso Básico de Python/Curso Básico de Python/Vendas/{arquivo}')
        tabela_total = pd.concat([tabela_total, tabela])
 
tabela_total = tabela_total.groupby('Produto').sum()
tabela_total = tabela_total[['Quantidade Vendida' , 'Preco Unitario']].sort_values(by='Quantidade Vendida' , ascending=False)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento' , ascending=False)
print(tabela_total)

