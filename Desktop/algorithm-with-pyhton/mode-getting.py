#Girilen sayının istenilen sayıya göre mod işlemini yaptıran programın algoritma ve akış diyagramını çiziniz.
#mod alma nedir? mod alma ikı sayının bölümünden kalandır. 3=(2.1)+1

dividend=int(input("Enter dividend number: ")) #bölünen
divisor=int(input("Enter divisor number: ")) #bölen

remainder=dividend # kalan
    
while remainder >= divisor :
    remainder-=divisor
    
    
print("Mode:" ,remainder )