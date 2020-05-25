import numpy as np

data_types = [('name', 'S15'), ('height', float), ('class', int)]
students = [('Mohsin', 181.2, 12), ('Ameya', 175.9, 11),('Yash', 133.4, 7), ('Palaash', 120.1, 11)]

students = np.array(students, dtype = data_types)   
print("Original array : ")
print(students)

print("On sorting by height : ")
print(np.sort(students, order='height')) 