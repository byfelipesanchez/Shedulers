def send_email():
    port = 465

    sender, password = 'senderemailfs@gmail.com', 'FelipeSanchezsSenderEmail'

    recieve = '2018.felipe.sanchez@gmail.com'

    message = '''\
    Subject: Testing Python Email

    Message via Python!

    Felipe

    '''

    context = ssl.create_default_context()

    print("starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)

    print("email sent!")