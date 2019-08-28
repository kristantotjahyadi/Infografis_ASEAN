import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'alfaindah25',
    database = 'world')

kursor = dbku.cursor()


# ========================= SOAL NOMOR 1 =========================== #
# populasi = []
# negara = []
# kursor.execute('''select Name, Population from country where Region = "Southeast Asia" order by Name''')
# data = kursor.fetchall()
# for item in data:
#     negara.append(item[0])
#     populasi.append(item[1])

# plt.style.use('seaborn')
# plt.bar(negara,populasi,color=['red','blue','green','gray','black','pink','purple','silver','gold','yellow'])
# plt.xticks(rotation=60)
# plt.title('Populasi Negara ASEAN')
# plt.xlabel('Negara')
# plt.ylabel('Populasi (x100jt jiwa)')
# plt.grid(True)
# ax = plt.gca()
# for p in ax.patches:
#     ax.annotate(str(p.get_height()), (p.get_x()*1.005,p.get_height()*1.005))
# plt.subplots_adjust(bottom=.2,right=.93)
# plt.show()


# ========================= SOAL NOMOR 2 =========================== #

# populasi = []
# negara = []
# kursor.execute('''select Name, Population from country where Region = "Southeast Asia" order by Name''')
# data = kursor.fetchall()
# for item in data:
#     negara.append(item[0])
#     populasi.append(item[1])

# warna = ['r', 'lightpink', 'pink', 'lightcoral','orange','gray','purple','blue','green','yellow']
# plt.pie(populasi,labels=negara,colors=warna,startangle=0,counterclock=True,autopct='%1.1f%%',textprops={'color':'k'}) 

# fig = plt.gcf()
# fig.set_size_inches(10,10)


# plt.title('Presentase Penduduk ASEAN')
# plt.grid(True)
# plt.show()


# ========================= SOAL NOMOR 3 =========================== #

# qry = ('''select Name, GNP from country where Region = "Southeast Asia" order by Name''')
# df = pd.read_sql(qry,con=dbku)
# plt.figure(figsize=(18,12))
# warna = ['b','orange','black','r','purple','brown','pink','gray','green','lightblue','yellow']
# plt.style.use('seaborn')
# plt.bar(df['Name'],df['GNP'],width=.6,color=warna)
# plt.xticks(rotation=60)
# plt.xlabel('Negara')
# plt.ylabel('Gross National Product (US$)')
# plt.title('Pendapatan Bruto Nasional ASEAN')
# ax = plt.gca()
# for p in ax.patches:
#     ax.annotate(str(p.get_height()), (p.get_x()*1.015,p.get_height()*1.005))
# plt.subplots_adjust(bottom=.15)
# plt.show()

# ======================== SOAL NOMOR 4 ============================= #

qry = ('''select Name, SurfaceArea from country where Region = "Southeast Asia" order by Name''')
df = pd.read_sql(qry,con=dbku)

warna = ['r', 'lightpink', 'pink', 'lightcoral','orange','gray','purple','blue','green','yellow']
plt.pie(df['SurfaceArea'],labels=df['Name'],colors=warna,autopct='%1.1f%%',textprops={'color':'k'})
plt.title('Persentase Luas Daratan ASEAN')
fig = plt.gcf()
fig.set_size_inches(10,10)
plt.show()
