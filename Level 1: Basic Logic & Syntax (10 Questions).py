#1.Check if a number is even or odd

checkNo = int(input("Enter any no. :"))
if(checkNo % 2 == 0) :
    print("It's Even No.")
else:
    print("It's Odd No.")   

#2.Find the largest of 3 numbers

a = int(input("Enter 1st No.:- "))
b = int(input("Enter 2nd No.:- "))
c = int(input("Enter 3rd No.:- "))
if a >= b and a >= c:
    print("Largest No. is :-", a)
elif b >=  a and b>= c:
    print("Largest No. is :-", b)
else:
    print("Largest No. is :-", c)  

#3.Print factorial of a number

n = int(input("Enter No.:"))
fact = 1
i=1
while i <= n:
    fact *= i
    i += 1
    
print("factorial is:",fact)

#4.Print Fibonacci series

n = int(input("Enter how many terms you want:"))
a = 0
b = 1
i = 0
while i < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    i += 1

#5.Reverse a number

num = int(input("Enter a no.: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = (rev * 10) + digit
    num = num // 10

print("Reversed no.: ",rev)

#6.Count digits in a number

num = int(input("Enter a no.: "))
count = 0

while num != 0:
   count += 1
   num = num // 10

print("total digit: ",count)

#7.Check if a year is leap year

year = int(input("Enter a year: "))

if(year % 400 == 0):
     print("it's a leap year.")  
elif(year % 100 == 0):   
     print("it's not a leap year.") 
elif (year % 4 == 0):
    print("it's a leap year.")     
else:
    print("it's not a leap year.")

#8.Print all prime numbers till 100

print("prime numbers from 1 to 100 are : ")
for num in range (50,101):
    is_prime = True
    for i in range (2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num,end=" ")    

#9.GCD of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD is:", gcd)

#10.Sum of digits in a number

n = int(input("Enter a number: "))
sum = 0

while n > 0:
    digit = n % 10      # get the last digit
    sum += digit        # add it to sum
    n = n // 10         # remove the last digit

print("Sum of digits is:", sum)
