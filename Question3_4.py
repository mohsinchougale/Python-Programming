import numpy as np
import matplotlib.pyplot as plt


moisturizer_data=np.genfromtxt('company_sales_data.csv',delimiter=',',skip_header=1,usecols=(6),dtype=int)
facecream_data=np.genfromtxt('company_sales_data.csv',delimiter=',',skip_header=1,usecols=(1),dtype=int)
months=np.genfromtxt('company_sales_data.csv',delimiter=',',skip_header=1,usecols=(0),dtype=int)
plt.hist([moisturizer_data,facecream_data],bins=[1000,1500,2000,2500,3000,3500,4000],label=['Moisturizer','Facecream'],color=['blue','pink'])
plt.legend(loc='upper right')
plt.xlabel('No. of Units ')
plt.ylabel('Frequency')
plt.title("Histogram for Frequency of products being sold for given unit range")
plt.show()