#Fibonacci serisinin ilk 10 terimini ekrana basan program.
#fibonacci dizisi nedir? ilk deger 0 ikinci deger 1 olmak uzere her ardışık elemanı 
#daha önceki iki elemanın toplamıdır.
#0,1,1,2,3,5,8,13 şeklinde ilerler.

num1=0
num2=1
print(num1,num2,sep="\n")

for i in range(8):
    num3=num1+num2
    print(num3)
    num1=num2
    num2=num3
    