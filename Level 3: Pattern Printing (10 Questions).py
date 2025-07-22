#1.Print triangle of *

n = int(input("Enter no. of rows: "))
for i in range(1, n+1):
    print("*" * i )

#2.Print inverted triangle

n = int(input("Enter no. of rows: "))    
for i in range(n, 0, -1):
    print("*" * i)

#3.Number pyramid    

n = int(input("Enter no. of rows: "))
for i in range(1, n+1 ):
    print(" " * (n-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#4.Floyd's triangle:Floyd's Triangle is a right-angled triangle made using consecutive natural numbers starting from 1.

n = int(input("Enter no. of rows:"))
num = 1
for i in range (1 , n+1):
    for j in range (1, i+1):
        print(num, end = " ")
        num += 1
    print()    

#5.Hollow square pattern

n = int(input("Enter the size of square: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
