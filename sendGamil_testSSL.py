import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd
from jinja2 import Template
import base64

# Configuración del servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 465  # Puerto para SSL
smtp_user = "onebyteventures@gmail.com"
smtp_password = "fhhn ibca dtpn arlw"

# Lista de Excel
# Leer la base de datos
email_df = pd.read_excel("files/emails.xlsx")
destinatarios = email_df['Email']

# Contenido del correo
asunto = "Asunto YOY, qué asunto ponemos?"
with open("files/email.html", "r", encoding='utf-8') as file:
    template = Template(file.read())

with open("files/foot_image.png", "rb") as imagen:
        logoFootpy = base64.b64encode(imagen.read()).decode()

cuerpo = template.render(
        logoFoot  = logoFootpy
        )


# Función para enviar el correo
def enviar_correo(destinatario):
    mensaje = MIMEMultipart()
    mensaje['From'] = smtp_user
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    
    # mensaje.attach(MIMEText(cuerpo, 'plain'))
    mensaje.attach(MIMEText(cuerpo, 'html')) # Especificamos el tipo de texto en HTML
    
    # Agregamos la firma como documento interno (no adjunto)
    
        

    try:
        servidor = smtplib.SMTP_SSL(smtp_server, smtp_port)
        servidor.login(smtp_user, smtp_password)
        servidor.sendmail(smtp_user, destinatario, mensaje.as_string())
        servidor.quit()
        print(f"Correo enviado a {destinatario}")
    except Exception as e:
        print(f"Error al enviar el correo a {destinatario}: {e}")

# Enviar correos a todos los destinatarios
for destinatario in destinatarios:
    enviar_correo(destinatario)
