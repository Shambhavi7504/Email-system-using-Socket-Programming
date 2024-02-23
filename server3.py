import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import ssl

# Setup port number and server name
smtp_port = 465                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

# Set up the email lists
email_from = "shambhaviraikar77@gmail.com"
email_list = ["kamakshishirodkar77@gmail.com", "sheelam@pes.edu", "nehams2004@gmail.com"]

# Define the password (better to reference externally)
pswd = "uyce bjyn mzhi epgc" # As shown in the video this password is now dead, left in as example only

# Name the email subject
subject = "New email from TIE with attachments!!"

# Define the path to your SSL certificate and key files
ssl_certfile = 'server_cert.pem'
ssl_keyfile = 'server_key.pem'

# Define the email function
def send_emails(email_list):
    # Create SSL context with your certificate and key
    ssl_context = ssl.create_default_context()
    ssl_context.load_cert_chain(certfile=ssl_certfile, keyfile=ssl_keyfile)

    for person in email_list:
        # Make the body of the email
        body = """
        line 1
        line 2
        line 3
        etc
        """

        # Make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))

        # Define the file to attach
        filename = "random_data.csv"

        # Open the file in python as a binary
        with open(filename, 'rb') as attachment:
            # Encode as base 64
            attachment_package = MIMEBase('application', 'octet-stream')
            attachment_package.set_payload(attachment.read())
            encoders.encode_base64(attachment_package)
            attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
            msg.attach(attachment_package)

        # Cast as string
        text = msg.as_string()

        # Connect with the server using SSL/TLS
        print("Connecting to server...")
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl_context) as TIE_server:
            TIE_server.login(email_from, pswd)
            print("Successfully connected to server")
            print()

            # Send emails to "person" as list is iterated
            print(f"Sending email to: {person}...")
            TIE_server.sendmail(email_from, person, text)
            print(f"Email sent to: {person}")
            print()

# Run the function
send_emails(email_list)
