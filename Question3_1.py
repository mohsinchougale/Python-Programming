import numpy as np
import matplotlib.pyplot as plt

bathing_soap_data=np.genfromtxt('company_sales_data.csv',delimiter=',',skip_header=1,usecols=(4),dtype=int)
months=np.genfromtxt('company_sales_data.csv',delimiter=',',skip_header=1,usecols=(0),dtype=int)
plt.bar(months,bathing_soap_data, label='Bathing Soap sales data')
plt.legend(loc='upper left')
plt.bar(months,bathing_soap_data)
plt.xlabel('Month number')
plt.ylabel('Sales data')
plt.title("Sales Data")
plt.grid()
plt.xticks(months)
plt.show()
