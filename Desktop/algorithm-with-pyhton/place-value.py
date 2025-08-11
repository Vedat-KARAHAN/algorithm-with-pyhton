#4 haneli bir sayının birler, onlar, yüzler ve binler hanesini bulan programı

number=input("Enter a 4-digits number:")

if '-' in number:
    sign='-'
    number=number.replace('-','')
else:
    sign='+'
    
if len(number)==4 and number.isdigit():
    thousands=int(number[0])*1000
    hundreds=int(number[1])*100
    tens=int(number[2])*10
    ones=int(number[3])
    print(f'{number} = ({sign}) * ({thousands} + {hundreds} + {tens} + {ones})')
else:
    print('Numbers must consist of digits!')




    
    