# Automações com python que vão Salvar seu tempo no trabalho
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 1. Automação de E-mais
def enviar_email():
    remetente = 'jppsc2005@gmail.com' # Corrigi a grafia para 'remetente'
    senha = "fyhu bjir bams tebn"
    destinatario = "gomesdasilvadeoliveiraj@gmail.com"
    assunto = "relatorio de vendas"
    corpo = "Este é um email automatico do relatorio de vendas do dia de hj"

    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario   
    mensagem["Subject"] = assunto   
    mensagem.attach(MIMEText(corpo, "plain"))

    # Atenção: "smpt.gmail.com" está errado, o correto é "smtp.gmail.com"
    servidor = smtplib.SMTP("smtp.gmail.com", 587) 
    servidor.starttls()
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatario, mensagem.as_string())
    servidor.quit()
    print("Email enviado com sucesso")

# Chame a função para executar a automação
enviar_email()
