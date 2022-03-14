import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
mesaj = MIMEMultipart()

mesaj["From"] = "" # mail kimden gidecek
def mail(n,s,i,b,p,skin,g,a,blo,d,phon,m,sonuc):
    sonuc_=""
    if(sonuc==1):
        sonuc_="Pozitif. En kısa sürede bunu teyit ettirmek adına yetkili hekiminize başvurmalısınız."
    else:
        sonuc_="Negatif. Sağlığınız iyi durumda.Bunu teyit ettirmek adına yetkili hekime başvurmalısınız."
    mesaj["To"] = m
    mesaj["Subject"] = "Makine öğrenmesi projesi"
    yazi = """
    Sayın {} {},
    Aşağıda bizlere vermiş olduğunuz bilgiler bulunmaktadır.
    NAME={}
    SURNAME={}
    INSULIN={}
    BMI={}
    PREGNANCIE={}
    SKIN_THICKNESS={}
    GLUCOSE={}
    AGE={}
    BLOOD_PRESSURE={}
    DPF={}
    PHONE_NUMBER={}
    MAIL={}
    
    Sonucunuz={}
        """.format(n,s,n,s,i,b,p,skin,g,a,blo,d,phon,m,sonuc_)
    mesaj_govdesi = MIMEText(yazi,"plain")
    mesaj.attach(mesaj_govdesi)
    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("","") # mail ve password
        mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
        print("Mail Başarıyla Gönderildi....")
        mail.close()

    except:
        sys.stderr.write("Bir sorun oluştu!")
        sys.stderr.flush()







