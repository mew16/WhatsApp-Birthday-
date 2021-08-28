import pandas as pd
from datetime import date
import time
import pywhatkit as pw
today = date.today()
d1 = today.strftime("%d/%m/%Y")
data = pd.read_csv("C:/Users/Mew/Desktop/birthday.csv")
uzunluk = len(data["Tarih"])
counter = 0
in_counter = 0
who_sended = list()
for i in range(0,uzunluk):
    if data.iloc[i,1] == d1[0:5]:
        in_counter += 1
        phone_number = data.iloc[i,3]
        pw.sendwhatmsg_instantly(f"+90{phone_number}",data.iloc[i,2],tab_close = True,wait_time = 7)
        who_sended.append(data.iloc[i,0])
        continue
    counter += 1
if counter >= 1 and in_counter < 1:print(f"Doğum Günü Henüz Gelmemiş Olanlar Sayısı = {counter}")
if in_counter >= 1:
    print("*"*20)
    print("Who Take Their Message")
    print("*"*20)
    for i in who_sended:
        print(i)
