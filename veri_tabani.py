import sqlite3
import os
os.chdir("C:/Users/omerm/Desktop")
class database():
    def __init__(self):
        self.baglanti_kur()
    def baglanti_kur(self):
        self.connect=sqlite3.connect("Veriler.db")
        self.cursor=self.connect.cursor()
        self.cursor\
            .execute("create table if not exists tablo "
                     "(name text,surname  text,mail text , Pregnancies int,Glucose int,BloodPressure int,SkinThickness int,Insulin int,BMI int,DiabetesPedigreeFunction int,Age int,Outcome int)")
        self.connect.commit()
    def veri_ekle(self,name,surname ,mail , Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome):
        self.cursor.execute("insert into tablo values(?,?,?,?,?,?,?,?,?,?,?,?)",(name,surname ,mail , Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome))
        self.connect.commit()
    def veri_sil(self,a):
        self.cursor.execute("delete from tablo where name=?",(a,))
        self.connect.commit()
deneme=database()
