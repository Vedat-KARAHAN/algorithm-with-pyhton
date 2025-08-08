#Sayı bulmaca oyunu programı

import random

i=1
rnd_number=random.randint(1, 100)


while i <= 10:
    estimate=int(input("Enter your estimate:"))    
    
    if estimate > rnd_number:
        print("Reduce estimate!")
    elif estimate < rnd_number:
        print("Increase estimate!")
    else:
        print(f"Congratulations,you found it in {i} tries")
        break
    i+=1