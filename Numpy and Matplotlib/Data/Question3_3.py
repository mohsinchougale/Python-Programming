import numpy as np
import matplotlib.pyplot as plt


shampoo_data=np.genfromtxt('company_sales_data.csv',delimiter=',',skip_header=1,usecols=(5),dtype=int)
months=np.genfromtxt('company_sales_data.csv',delimiter=',',skip_header=1,usecols=(0),dtype=int)
moist_data=np.genfromtxt('company_sales_data.csv',delimiter=',',skip_header=1,usecols=(6),dtype=int)
plt.scatter(months,shampoo_data,color='orange',label='Shampoo')
plt.scatter(months,moist_data,color='green',label='Moisturiser')
plt.legend(loc='upper right')
plt.xlabel('Month number')
plt.ylabel('Sale units')
plt.title("Scatter plot for Shampoo & Moisturiser")
plt.grid()
plt.xticks(months)
plt.show()
