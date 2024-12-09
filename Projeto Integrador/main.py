import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Função para ler os dados de um arquivo CSV
def leitura_de_dados(arquivo_csv):
    df = pd.read_csv(arquivo_csv)
    return df

# Função para analisar os dados e atribuir níveis
def analise_de_dados(df, estoque_critico, estoque_alerta):
    # Atribuir níveis de alerta
    df['nivel_esteira1'] = df['esteira1'].apply(lambda x: 0 if x == 0 else (1 if x <= estoque_critico else 2))
    df['nivel_esteira2'] = df['esteira2'].apply(lambda x: 0 if x == 0 else (1 if x <= estoque_critico else 2))
    df['nivel_esteira3'] = df['esteira3'].apply(lambda x: 0 if x == 0 else (1 if x <= estoque_critico else 2))

    # Filtrar as esteiras com nível crítico ou abaixo
    esteiras_abaixo_critico = df[df[['nivel_esteira1', 'nivel_esteira2', 'nivel_esteira3']].isin([0, 1]).any(axis=1)]
    return esteiras_abaixo_critico

# Função para gerar alertas em tela
def gerar_alertas_em_tela(esteiras_abaixo_critico, estoque_critico, estoque_alerta):
    if not esteiras_abaixo_critico.empty:
        for index, row in esteiras_abaixo_critico.iterrows():
            for esteira in ['esteira1', 'esteira2', 'esteira3']:
                nivel = row[f'nivel_{esteira}']
                if nivel == 0:
                    print(f"ALERTA: Estoque da {esteira} acabou. Nível atual: {row[esteira]}")
                elif nivel == 1:
                    print(f"ALERTA: Estoque da {esteira} está no nível crítico. Nível atual: {row[esteira]}")
                elif nivel == 2:
                    print(f"ALERTA: Estoque da {esteira} está em alerta. Nível atual: {row[esteira]}")

# Função para enviar alertas por email
def enviar_alerta_email(esteiras_abaixo_critico, estoque_critico, estoque_alerta):
    if not esteiras_abaixo_critico.empty:
        sender_email = "lucasnareli@gmail.com"
        receiver_email = "leoaviana1206@gmail.com"
        password = "ygjj bwtn afvl pgda"

        # Configuração do servidor de email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        for index, row in esteiras_abaixo_critico.iterrows():
            for esteira in ['esteira1', 'esteira2', 'esteira3']:
                nivel = row[f'nivel_{esteira}']
                if nivel == 0:
                    subject = f"ALERTA: Estoque da {esteira} acabou"
                    body = f"O estoque da {esteira} acabou.\nNível atual: {row[esteira]}."
                elif nivel == 1:
                    subject = f"ALERTA: Estoque da {esteira} no nível crítico"
                    body = f"O estoque da {esteira} está no nível crítico.\nNível atual: {row[esteira]}."
                elif nivel == 2:
                    subject = f"ALERTA: Estoque da {esteira} em alerta"
                    body = f"O estoque da {esteira} está em alerta.\nNível atual: {row[esteira]}."

                # Criar o conteúdo do email
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                # Enviar o email
                server.sendmail(sender_email, receiver_email, msg.as_string())

        server.quit()

# Função para gerar um relatório de alertas em Excel
def gerar_relatorio(esteiras_abaixo_critico):
    if not esteiras_abaixo_critico.empty:
        data_atual = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        nome_relatorio = f"relatorio_alertas_{data_atual}.xlsx"
        esteiras_abaixo_critico.to_excel(nome_relatorio, index=False)
        print(f"Relatório gerado: {nome_relatorio}")
    else:
        print("Nenhum alerta gerado. Nenhuma esteira com estoque abaixo do crítico.")

# Função principal para automatizar o processo
def automatizar_processos_logisticos(arquivo_csv, estoque_critico, estoque_alerta):
    df = leitura_de_dados(arquivo_csv)
    esteiras_abaixo_critico = analise_de_dados(df, estoque_critico, estoque_alerta)

    gerar_alertas_em_tela(esteiras_abaixo_critico, estoque_critico, estoque_alerta)
    enviar_alerta_email(esteiras_abaixo_critico, estoque_critico, estoque_alerta)
    gerar_relatorio(esteiras_abaixo_critico)

arquivo_csv = 'Esp8266_Receiver.csv'
estoque_critico = 1
estoque_alerta = 2
automatizar_processos_logisticos(arquivo_csv, estoque_critico, estoque_alerta)