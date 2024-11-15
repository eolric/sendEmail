import smtplib
import pandas as pd

# Set credentials - establecer variables para la conexión al gmail
name_account = "Sandreke"
email_account = "sandreke99@gmail.com"
password_account = "zmpwpbqxfdnoxpha" # password created in step 1.3.

# 'smtp.gmail.com' and 465 port refer to Gmail as provider
# Change these arguments if you are using another one
# For example, Outlook arguments are 'smtp-mail.outlook.com' and 587 port
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(email_account, password_account)

# Read the file that contains at least names & email addresses
# Subjects & messages can be personalized, but we use them as input
email_df = pd.read_excel("Data/Emails.xlsx")

# Get all names, email addresses, subjects & messages
all_names = email_df['Name']
all_emails = email_df['Email']
all_subjects = email_df['Subject']
all_messages = email_df['Message']