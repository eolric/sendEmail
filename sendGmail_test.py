import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587  # o 465 para SSL
smtp_user = "onebyteventures@gmail.com"
smtp_password = "fhhn ibca dtpn arlw"

# Lista de destinatarios
destinatarios = ["eoglc15@gmail.com"]

# Contenido del correo
asunto = "Asunto del correo"
cuerpo = "Este es el cuerpo del correo."

# Función para enviar el correo
def enviar_correo(destinatario):
    mensaje = MIMEMultipart()
    mensaje['From'] = smtp_user
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    
    try:
        servidor = smtplib.SMTP(smtp_server, smtp_port)
        servidor.starttls()  # Inicio de la conexión segura
        servidor.login(smtp_user, smtp_password)
        servidor.sendmail(smtp_user, destinatario, mensaje.as_string())
        servidor.quit()
        print(f"Correo enviado a {destinatario}")
    except Exception as e:
        print(f"Error al enviar el correo a {destinatario}: {e}")

# Enviar correos a todos los destinatarios
for destinatario in destinatarios:
    enviar_correo(destinatario)
