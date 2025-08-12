#10 ile 100 arasındaki tam kare sayıları ekrana yazdıran program
#Tam kare sayı nedir? karekök dışına çıkan sayılara denir.
from math import sqrt

for i in range(10,101):
    temp=(sqrt((i)))
    if temp.is_integer():
        print(i,"Is a perfecet square")
