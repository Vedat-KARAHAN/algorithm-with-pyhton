# 1-100 arasındaki çift sayıların toplamının mükemmel sayı olup olmadığını bulan program.
#mukemmel sayı nedir? kendisi harıc pozıtıf bolenlerıne esıt olan sayılara denır.
num=0
divisors=0
for i in range(0,101,2):
    num+=i
    
    
for i in range(1,int(num/2)+1):
    if num % i == 0:
        divisors+=i

if num == divisors:
    print("It is a perfect number!")
else:
    print("It is not a perfect number!")
    