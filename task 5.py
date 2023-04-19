import numpy as np
list=np.array(['Хлеб', 'колбаса', 'молоко', 'жвачка', 'печенье', 'картошка'])
count=len(list)
for i in range(count):
    if(len(list[i])%2==0):
        print(list[i])
