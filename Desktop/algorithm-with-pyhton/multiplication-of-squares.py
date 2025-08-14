#1 ile 25 arasındaki tam sayıların karelerinin çarpımını bulan program.

multiples=1

for i in range(2,25):
    multiples *= i**2

print(multiples)