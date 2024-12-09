#12/11/2024

#Exercício 1

"""with open("teste.txt", "w") as arquivo:
    arquivo.write("Ola mundo!\n")
    arquivo.write("Aprendendo Python")"""
from fileinput import close
from idlelib.iomenu import encoding

#Exercicio 2

"""with open("teste.txt", "r") as arquivo:
    leitura = arquivo.read()
    print(leitura)"""

#Exercicio 3

"""import csv

with open("produtos.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Nome", "Preço"])
    writer.writerow(["Livro", 20])"""

#Exercicio 4

"""import csv

with open("produtos.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)"""

#Exercicio 5

"""import json

dados = {
    "Nome" : "João",
    "Idade" : "25"
}

arquivo = open("dados.json", "w", encoding='UTF-8')
json.dump(dados,arquivo,ensure_ascii=False)
arquivo.close()"""

#Exercicio 6

"""import json

arquivo = open("dados.json", "r")
dados = json.load(arquivo)
arquivo.close()

print(dados)"""

#Exercicio 7

"""import xml.etree.ElementTree as ET

config = ET.Element("config")
versao = ET.SubElement(config,"versao")
versao.text = str(1)

teste = ET.ElementTree(config)
teste.write('novo_arquivo.xml', encoding='utf-8', xml_declaration=True)"""

#Exercico 8

"""import xml.etree.ElementTree as ET

teste = ET.parse('novo_arquivo.xml')
leitura = teste.getroot()

versao = leitura.find("versao").text
print(f"Versão: {versao}")"""

#Exercicio 9

"""import pandas as pd

dados = {'Produto': ['Celular'],
         'Quantidade': [10]}

df = pd.DataFrame(dados)

df.to_excel('vendas.xlsx', index=False)

print("Arquivo 'vendas.xlsx' criado com sucesso!")"""

#Exercicio 10

"""import pandas as pd

df = pd.read_excel('vendas.xlsx', engine='openpyxl')

print(df)"""