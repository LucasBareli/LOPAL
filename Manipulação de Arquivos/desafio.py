#Lucas Duarte Bareli - Manipulação de Arquivos

#Exercicio 1

"""with open("aula.txt", "w",encoding='utf-8') as arquivo:
    arquivo.write("Python é Legal!\n")
    arquivo.write("Aprendendo Manipulações de Arquivos")"""

#Exercicio 2

"""with open('aula.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

print(conteudo)"""

#Exercicio 3

"""import csv

with open("alunos.csv","w", newline="") as alunos:
    writer = csv.writer(alunos)
    writer.writerow(["Nome", "Idade"])
    writer.writerow(["João", 20])
    writer.writerow(["Maria", 22])"""

#Exercicio 4

"""import csv

with open("alunos.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)"""

#Exercicio 5

"""import json

info = {
    "Gato" : "Felix",
    "Cachorro" : "Rex"
}

arquivo = open("info.json", "w", encoding='UTF-8')
json.dump(info,arquivo,ensure_ascii=False)
arquivo.close()"""

#Exercicio 6

"""import json

arquivo = open("info.json", "r")
info = json.load(arquivo)
arquivo.close()

print(info)"""

#Exercicio 7

"""import xml.etree.ElementTree as ET

elementos = ET.Element("Elementos")

hidro = ET.SubElement(elementos, "Hidrogênio")
hidro.text = ""

oxi = ET.SubElement(elementos, "Oxigênio")
oxi.text = ""

teste = ET.ElementTree(elementos)

teste.write('elementos.xml', encoding='utf-8', xml_declaration=True)"""

#Exercicio 8

"""import xml.etree.ElementTree as ET

teste = ET.parse('elementos.xml')
leitura = teste.getroot()

for elemento in leitura:
    print(f"Elemento: {elemento.tag}")"""

#Exercicio 9

"""import pandas as pd

dados = {'Alunos': ['Lucas', 'Marcia'],
         'Nota_port': [10, 0],
         'Nota_mat': [10, 0]
        }

df = pd.DataFrame(dados)

df.to_excel('notas.xlsx', index=False)"""

#Exercicio 10

"""import pandas as pd

df = pd.read_excel('notas.xlsx', engine='openpyxl')

print(df)"""

#DESAFIOS

#Desafio 1

"""import pandas as pd

historico_pedidos = [

{'ID': 1, 'Nome': 'João', 'Endereço': 'Rua das Flores, 123', 'Produto': 'Camiseta', 'Quantidade': 2, 'Preço': 50, 'Data': '01/01/2023'},

{'ID': 2, 'Nome': 'Mariana', 'Endereço': 'Avenida Central, 456', 'Produto': 'Tênis', 'Quantidade': 1, 'Preço': 120, 'Data': '02/01/2023'},

{'ID': 3, 'Nome': 'Carlos', 'Endereço': 'Praça da Estação, 789', 'Produto': 'Mochila', 'Quantidade': 1, 'Preço': 80, 'Data': '03/01/2023'},

{'ID': 4, 'Nome': 'Fernanda', 'Endereço': 'Alameda dos Anjos, 101', 'Produto': 'Relógio', 'Quantidade': 1, 'Preço': 150, 'Data': '04/01/2023'}

]

df = pd.DataFrame(historico_pedidos)

df.to_excel('compras.xlsx', index=False)"""

#Desafio 2

"""import pandas as pd

df = pd.read_excel('compras.xlsx')

df.to_csv('compras.csv', index=False)"""

#Desafio 3

"""import pandas as pd

df = pd.read_csv('compras.csv')

df.to_json('compras.json', orient='records', lines=True)"""

#Desafio 4

"""with open("criptografado.txt", "w", encoding="UTF-8") as arquivo:
    criptografia = ". Sru txh rv ghvhqvroyhgruhv mâr jrvwdp gh vduu dr du olyuh? Srutxh r pxqgr uhdm whp pxlwrv exjv.
. Frpr yrm fghp lhghqwlihdu xp surjudpdgru hawuryhuwlgr? Hoh rokd sduu rv VHXV vdsdwrv hqtdqwpr idod frp yrm.
. R txh r surjudpdgru Sbwkrq glvvh txdqgr hqfrqwurx xpd frpud? "Dk, é dsqdv xpdu hiuhthqfdd!"
. Frpr yrm ida xp surjudpdgru vruulu? Gljd: "Roi, Pxqgr!"
. Frpr rv surjudpdgruhv vh ghvshehp? "ebwh ebwh!"
. Frpr rv surjudpdgruhv hawuhvvdp vhx dpru? "Hqtxdqwpr (fruddmr.dlqgdEdwh()) { hx.whDpr(); }"
. Sru txh rv surjudpdgruhv rghldp hvsdorv? Srutxh holv suhihupw wdev!
. Frpr yrm frpiruwdu xp ghvhqvroyhgru MdydVfulsw? "Mâr vh suhrfxsh, ydl ilfdu wxgr 'xqghilqhg'."
. R txh r KPWB glvvh dr FVV? "Yrm sdeh frpr ph idahu sduhfhu erp!"
. Sru txh r edqfr gh gdgrv vh mxqwrx dr Wlqghu? Hoh hvwdyd surfxudqgr xpdu uhoodmp!
. R txh d ixomr glvvh diyv vhu fkdpdgd? "Hx uhwrudp!""
    arquivo.write(criptografia)


def descriptografar_cifra_cesar(texto_criptografado, deslocamento):
    texto_descriptografado = ''

    for char in texto_criptografado:
        if char.isalpha():
            deslocamento_base = 65 if char.isupper() else 97
            novo_char = chr((ord(char) - deslocamento_base - deslocamento) % 26 + deslocamento_base)
            texto_descriptografado += novo_char
        else:
            texto_descriptografado += char

    return texto_descriptografado


def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
        return None

nome_arquivo = 'criptografado.txt'

texto_criptografado = ler_arquivo(nome_arquivo)

if texto_criptografado:
    deslocamento = 3
    texto_descriptografado = descriptografar_cifra_cesar(texto_criptografado, deslocamento)

    print("Texto Descriptografado:")
    print(texto_descriptografado)"""