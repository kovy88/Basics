import smtplib


#pepik.nov123@gmail.com

# koval.macek@seznam.cz



my_email = "pepik.nov123@gmail.com"
password = "wdreowbtgawezfnc"
message = "Subject: Dulezita zprava\n\nAhoj, "


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(my_email,
                        "koval.macek@seznam.cz",
                        message.encode("utf-8"))
























