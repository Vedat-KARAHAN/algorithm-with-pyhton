#Verilen yılın artık yıl olup olmadığını bulan program.
#artık yıl nedır? 1 yil 365 gün 6 saattır her yıldan kalan 6 saat
#4 senede bir 24 saat eder buda şubat ayına eklenır.

year=int(input("Enter a year:"))

if year % 4 == 0:
    print("The number entered is a leap year!")
else:
    print("The number entered is not a leap year!")

