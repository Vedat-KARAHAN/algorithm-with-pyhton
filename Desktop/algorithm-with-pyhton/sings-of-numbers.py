#Rastgele girilen 50 sayıdan negatif olanların ve pozitif olanların sayısını bulan program

positive_counter=0
negative_counter=0
zero_counter=0
for i in range(5):
    temp=int(input("Enter a number:"))
    if temp > 0:
        positive_counter +=1
    elif temp < 0:
        negative_counter +=1
    else:
        zero_counter +=1

print(f"Among the numbers entered there are {positive_counter} positive , {negative_counter} negative and {zero_counter} zeros")