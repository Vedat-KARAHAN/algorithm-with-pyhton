#klavyeden girilen sayının negatif,pozitif olup olmadıgını kontrol eden program.
#eger bir sayı 0 dan kucukse negatıf 0 dan buyukse pozıtıf 0 ise notrdür

num1=int(input("Enter number:"))

if num1 > 0:
    print(num1," is a positive number")
elif num1 < 0:
    print(num1," is a negative number")
else:
    print(num1," is a neutral number")