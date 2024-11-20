import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd
from jinja2 import Template
# import base64

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
asunto = "Asunto YOY, invierte"
with open("files/email.html", "r", encoding='utf-8') as file:
    template = Template(file.read())

# with open("files/foot_image.png", "rb") as imagen:
#         logoFootpy = base64.b64encode(imagen.read()).decode()

# Renderizar el cuerpo HTML
cuerpo_html = template.render()

# cuerpo = template.render(
#         logoFoot  = logoFootpy
#         )


# Función para enviar el correo
def enviar_correo(destinatario, cuerpo_html):
    mensaje = MIMEMultipart('related')
    mensaje['From'] = smtp_user
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    
    # mensaje.attach(MIMEText(cuerpo, 'plain'))
    mensaje.attach(MIMEText(cuerpo_html, 'html')) # Especificamos el tipo de texto en HTML
    
    # Agregar imágenes con Content-ID 
    imagenes = [ 
        ("files/head_image.png", "head_YOY"), 
        ("files/iconWapp.png", "iWapp"), 
        ("files/foot_image.png", "firma_Innverto")
    ]
    
    for img_path, cid in imagenes: 
        with open(img_path, "rb") as img_file: 
            img = MIMEImage(img_file.read()) 
            img.add_header("Content-ID", f"<{cid}>") 
            img.add_header("Content-Disposition", "inline", filename=img_path.split('/')[-1]) 
            mensaje.attach(img)

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
    enviar_correo(destinatario, cuerpo_html)
