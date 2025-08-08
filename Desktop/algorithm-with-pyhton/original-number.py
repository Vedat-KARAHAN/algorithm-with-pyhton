#Girilen dört basamaklı sayılardan ilk iki basamağı ile son iki basamağının toplamının karesi, sayının kendine eşit olan sayılara orijinal sayı denir. Girilen sayının orijinal olup olmadıgını bulan program
#mesela abcd diye bir sayı girdi (ab+cd)^2=abcd ise orjinal sayıdır.

number=input("Enter a number:")

if len(number) == 4 and number.isdigit():
    begin=number[0]+number[1]
    last=number[2]+number[3]
    
    number=int(number)
    begin=int(begin)
    last=int(last)
    total=begin+last
    
    if total**2 == number:
        print("The entered number is original number")
    else:
        print("The entered number is not original number")

else:
    print("Enter 4 digits positive number")
