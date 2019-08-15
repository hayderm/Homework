import numpy as np 

'''
L1 : first list length 
L2 : second list length

'''
L1 = int(raw_input('Enter first list lenght:'))
L2 = int(raw_input('Enter second list lenght:'))

#generate first and second lists 
list1 = np.random.randint(1,high=10,size=L1,dtype=int)
list2 = np.random.randint(1,high=10,size=L2,dtype=int)
print list1
print list2
for y in list1:
    z = [y for x in list2 if y==x]
print z

