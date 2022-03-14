import numpy as np
import pandas as pd
import pickle

import numpy as np
def bmi(x):
    if(x<=18.5):
        return 3
    elif(x>18.5 and x<=24.9):
        return 4
    elif(x>25 and x<=29.9):
        return 1
    elif(x>30 and x<=39.9):
        return 0
    else:
        return 2
def insulin(x):
    if(x>=60 and x<=120):
        return 0
    return 1
def glucose(x):
    if(x<90):
        return 1
    elif(x>=90 and x<=125):
        return 2
    else:
        return 0
def bloodpressure(x):
    if(x>=70 and x<=90):
        return 2
    elif(x<70):
        return 1
    else:
        return 0
import pandas as pd
import pickle
def tahmin(preg,gluc,blood,skin,ins,bmi_,dmf,age):
    df=pd.DataFrame(np.zeros((8))).T
    df.columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']
    bmii=pd.DataFrame(np.zeros((5))).T
    bmii.columns=['bmi_obese','bmi_over-weight', 'bmi_severely obese', 'bmi_weak', 'bmi_weight']
    ins_=pd.DataFrame(np.zeros(1)).T
    ins_.columns=['insulin_anormal value']
    gluc_=pd.DataFrame(np.zeros((3))).T
    gluc_.columns=['glucose_high', 'glucose_low',
    'glucose_normal']
    bp=pd.DataFrame(np.zeros(3)).T
    bp.columns=[ 'bloodpressure_high', 'bloodpressure_low',
    'bloodpressure_normal']
    degerler=[preg,gluc,blood,skin,ins,bmi_,dmf,age]
    for i in range(len(degerler)):
        df.loc[:, df.columns[i]] = degerler[i]
    bp.iloc[:,bloodpressure(int(blood))]=1
    gluc_.iloc[:,glucose(int(gluc))]=1
    bmii.iloc[:,bmi(int(bmi_))]=1
    if(insulin(int(ins))==0):
        ins_.iloc[:,0]=0
    else:
        ins_.iloc[:, 0] = 1
    dosya = "model.kayit"
    yuklenen = pickle.load(file=open(dosya, "rb"))
    df=pd.concat((df,bmii,ins_,gluc_,bp),axis=1)


    return yuklenen.predict(df)

df=tahmin(500,500,500,500,500,500,500,500)

