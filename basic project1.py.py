#gmail sender
#smtp-> simple mail transfer proticol
import smtplib
sender_email="kurmaiahgariudayani@gmail.com"
receiver_email="kshanmukhreddy31@gmail.com"
password="wejwglyzywsevgaw"
subject="introduce"
message="this is udayani"
try:
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message,subject)
    print("email done")
    server.quit()
except Exception as e:
        print(e)
