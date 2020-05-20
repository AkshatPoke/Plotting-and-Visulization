import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import urllib.request as ur 
from bs4 import BeautifulSoup

oly_12 = 'https://en.wikipedia.org/wiki/United_States_at_the_2012_Summer_Olympics'
oly_16 = 'https://en.wikipedia.org/wiki/United_States_at_the_2016_Summer_Olympics'

wiki_page_12 = ur.urlopen(oly_12)
wiki_page_16 = ur.urlopen(oly_16)

s_12 = BeautifulSoup(wiki_page_12,'lxml')
s_16 = BeautifulSoup(wiki_page_16,'lxml')

tables_12 = s_12.find_all('table', class_ = 'wikitable')
tables_16 = s_16.find_all('table', class_ = 'wikitable')
need_table_12 = tables_12[1]
need_table_16 = tables_16[1]

a_12 = []
b_12 = []
c_12 = []
d_12 = []
e_12 = []
a_16 = []
b_16 = []
c_16 = []
d_16 = []
e_16 = []
for row_12 in need_table_12.find_all('tr'):
    cell_12 = row_12.find_all('td')
    if len(cell_12) == 5:
        a_12.append(cell_12[0].find(text = True))
        b_12.append(cell_12[1].find(text = True).strip())
        c_12.append(cell_12[2].find(text = True).strip())
        d_12.append(cell_12[3].find(text = True).strip())
        e_12.append(cell_12[4].find(text = True).strip())
for row_16 in need_table_16.find_all('tr'):
    cell_16 = row_16.find_all('td')
    if len(cell_16) == 5:
        a_16.append(cell_16[0].find(text = True))
        b_16.append(cell_16[1].find(text = True).strip())
        c_16.append(cell_16[2].find(text = True).strip())
        d_16.append(cell_16[3].find(text = True).strip())
        e_16.append(cell_16[4].find(text = True).strip())

df_12 = pd.DataFrame(a_12,columns=['Sport'])
df_12['Gold_2012'] = b_12
df_12['Silver_2012'] = c_12
df_12['Bronze_2012'] = d_12
df_12['Total_2012'] = e_12
df_12 = df_12[1:]
df_12 = df_12.reset_index()
df_12 = df_12.iloc[:,1:]
df_12[['Gold_2012','Silver_2012','Bronze_2012','Total_2012']] = df_12[['Gold_2012','Silver_2012','Bronze_2012','Total_2012']].astype(int)

df_16 = pd.DataFrame(a_16,columns=['Sport'])
df_16['Gold_2016'] = b_16
df_16['Silver_2016'] = c_16
df_16['Bronze_2016'] = d_16
df_16['Total_2016'] = e_16
df_16 = df_16[1:]
df_16 = df_16.reset_index()
df_16 = df_16.iloc[:,1:]
df_16[['Gold_2016','Silver_2016','Bronze_2016','Total_2016']] = df_16[['Gold_2016','Silver_2016','Bronze_2016','Total_2016']].astype(int)

print(df_12)
print(df_16)

df = pd.merge(df_12,df_16,how = 'inner')
print(df)

bar_width = 0.3
plt.figure()
sports = df['Sport']
y_pos = np.arange(len(sports))
p1_12 = plt.bar(y_pos,df['Gold_2012'],bar_width,align='center',alpha=0.4,color='gold')
p1_16 = plt.bar(y_pos+bar_width+0.05,df['Gold_2016'],bar_width,align='center',alpha=1,color='gold')
p2_12 = plt.bar(y_pos,df['Silver_2012'],bar_width,bottom = df['Gold_2012'].values.astype(np.float64),align='center',alpha=0.4,color='silver')
p2_16 = plt.bar(y_pos+bar_width+0.05,df['Silver_2016'],bar_width,bottom = df['Gold_2016'].values.astype(np.float64),align='center',alpha=1,color='silver')
p3_12 = plt.bar(y_pos,df['Bronze_2012'],bar_width,bottom = df['Gold_2012'].values.astype(np.float64)+df['Silver_2012'].values.astype(np.float64),align='center',alpha=0.4,color='brown')
p3_16 = plt.bar(y_pos+bar_width+0.05,df['Bronze_2016'],bar_width,bottom = df['Gold_2016'].values.astype(np.float64)+df['Silver_2016'].values.astype(np.float64),align='center',alpha=1,color='brown')

plt.xticks(y_pos + bar_width/2 , sports, rotation ='vertical')
plt.ylabel('Number of Medals')
plt.title('US Olympic Medals by Sports')
plt.legend((p1_12[0],p1_16[0],p2_12[0],p2_16[0],p3_12[0],p3_16[0]),('Gold 2012','Gold 2016','Silver 2012','Silver 2016','Bronze 2012','Bronze 2016'))
plt.show()
