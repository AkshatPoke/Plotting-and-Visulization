import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('./data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

minimum = []
maximum = []
df = df[~(df['Date'].str.endswith(r'02-29'))]
times = pd.DatetimeIndex(df['Date'])

df1 = df[times.year != 2015]
times1 = pd.DatetimeIndex(df1['Date'])
for i in df1.groupby([times1.month,times1.day]):
    minimum.append(min(i[1]['Data_Value']))
    maximum.append(max(i[1]['Data_Value']))

minimum2015 = []
maximum2015 = []

df2015 = df[times.year == 2015]
times2015 = pd.DatetimeIndex(df2015['Date'])
for j in df2015.groupby([times2015.month,times2015.day]):
    minimum2015.append(min(j[1]['Data_Value']))
    maximum2015.append(max(j[1]['Data_Value']))

minaxis = []
maxaxis = []
minvalue = []
maxvalue = []
for k in range(len(minimum)):
    if((minimum[k] - minimum2015[k]) > 0):
        minaxis.append(k)
        minvalue.append(minimum2015[k])
    if((maximum[k] - maximum2015[k]) < 0):
        maxaxis.append(k)
        maxvalue.append(maximum2015[k])

plt.figure()
colors = ['green','red']
plt.plot(minimum, c = 'green', alpha = 0.5, label = 'Minimum Temperature (2005-2014)')
plt.plot(maximum, c = 'red', alpha = 0.5, label = 'Maximum Temperature (2005-2014)')
plt.scatter(minaxis, minvalue, s = 10, c = 'blue', label = 'Record Break Minimum(2015)')
plt.scatter(maxaxis, maxvalue, s = 10, c ='black', label = 'Record Break Maximum(2015)')
plt.gca().fill_between(range(len(minimum)), minimum, maximum, facecolor = 'blue', alpha = 0.25)
plt.ylim(-400, 500)
plt.legend(loc = 8, frameon = False, title = 'Temperature', fontsize = 8)
plt.xticks(np.linspace(15, 15+30*11, num =12), (r'Jan', r'Feb', r'Mar', r'Apr', r'May', r'Jun', r'Jul', r'Aug', r'Sep', r'Oct', r'Nov', r'Dec'))
plt.xlabel('Months')
plt.ylabel('Temperature (tenths of degrees C)')
plt.title(r'Extreme temperature of "College Station, Texas" by months, with outliers')
plt.show()
