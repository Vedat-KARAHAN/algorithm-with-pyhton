#Çarpma işlemini toplama kullanarak bulan programın algoritma ve akış diyagramını çiziniz.
#Çarpma işlemi nasıl yapılır? 4x5=20=5+5+5+5=4+4+4+4+4

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
i=0
total=0
while i < num2 :
    total+=num1
    i+=1

print("Answer:",total)
    
    