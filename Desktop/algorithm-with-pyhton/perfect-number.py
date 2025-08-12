#Girilen sayının mükemmel sayı olup olmadığını bulan program.
#Mükemmel sayı nedir? kendisi harıc pozitif bolenleri kendısıne esıt olan sayılara denır.
#örn:6 mükemmel sayıdır çünkü 6=3+2+1

num=int(input("Enter number:"))

divisors=0
if num > 0:
        for i in range(1,num):
            if num % i ==0:
                divisors+=i
    
        if num == divisors:
            print("The Entered number is a perfect number!")
        else:
            print("The Entered number isn't a perfect number!")

else:
    print("The Entered number isn't a perfect number!")
