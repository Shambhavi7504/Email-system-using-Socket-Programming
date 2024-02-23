import smtplib
import ssl

smtp_port = 465  # 465 is the standard secure SMTP port for SSL
smtp_server = "smtp.gmail.com"  # Google SMTP Server
email_from = "shambhaviraikar77@gmail.com"
email_to = "nandini.edu2004@gmail.com"
pswd = "uyce bjyn mzhi epgc"
message = "Hi, how are you?"

# Path to your SSL certificate and key files
ssl_certfile = 'server_cert.pem'
ssl_keyfile = 'server_key.pem'

ssl_context = ssl.create_default_context()
ssl_context.load_cert_chain(certfile=ssl_certfile, keyfile=ssl_keyfile)

TIE_server = None

try:
    print("Connecting to server")
    TIE_server = smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl_context)
    TIE_server.login(email_from, pswd)
    print('Connected to server:')
    print()

    print(f"Sending email to {email_to}")
    TIE_server.sendmail(email_from, email_to, message)
    print(f"Email successfully sent to {email_to}")

except Exception as e:
    print(e)

finally:
    if TIE_server:
        # Close the connection
        TIE_server.quit()
