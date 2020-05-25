import numpy as np
import matplotlib.pyplot as plt

Total_prof_data=np.genfromtxt('company_sales_data.csv',delimiter=',',skip_header=1,usecols=(8),dtype=int)
months=np.genfromtxt('company_sales_data.csv',delimiter=',',skip_header=1,usecols=(0),dtype=int)
plt.plot(months,Total_prof_data)
plt.legend(loc='upper left')
plt.xlabel('Month number')
plt.ylabel('Total Profit')
plt.title("Total profit Monthly")
plt.grid()
plt.xticks(months)
plt.show()
