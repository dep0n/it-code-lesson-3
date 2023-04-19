import math
number=int(input())
index=0
for i in range(2, int(math.sqrt(number))+1):
    if (number%i==0):
        index+=1
        break
if (index==0):
    print("Простое")
else:
    print("Составное")
