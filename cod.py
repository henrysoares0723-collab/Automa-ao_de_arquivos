import os

lista_arquivos = os.listdir("Curso Básico de Python/Curso Básico de Python/Vendas")
print(lista_arquivos)
for arquivo in lista_arquivos:
    print(arquivo)
    print(f'Curso Básico de Python/Curso Básico de Python/Vendas/{arquivo}')
    if 'Vendas' in arquivo:
        print(f'Curso Básico de Python/Curso Básico de Python/Vendas/{arquivo}')
    else:
        print('Arquivo de devolução')


