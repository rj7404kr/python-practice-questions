#1.Reverse a string

string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("Reversed string is:", reversed_string)
 
#2.Check if string is palindrome

string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
if string == reversed_string:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")

#3.Count vowels and consonants in a string

string = input("enter a string:")
vowels = 0
consonants = 0
string = string.lower()
for char in string:
    if char.isalpha():
        if char in 'aeiou':
            vowels += 1
        else:
            consonants += 1    
print("vowels:",vowels) 
print("consonatnts:",consonants)               

#4.Remove duplicate characters from string

string = input("Enter a string: ")
result = ""

for char in string:
    if char not in result:
        result += char

print("String after removing duplicates:", result)

#5.Find frequency of each character in string

string = input("Enter a string: ")
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char, count in frequency.items():
    print(f"{char}: {count}")

#6.Find largest word in a string
 
string = input("Enter a string:")
words = string.split()
largest = ""
for word in words:
    if len(word) > len(largest):
        largest = word
print("largest word:",largest)
print("Length;",len(largest))

#7. Sort a list using sort()

numbers = [8,3,9,1,0,4,5,7]
numbers.sort()
print("sorted no:",numbers)

#8. Sort a list without using sort()

numbers = [8, 3, 9, 1, 0, 4, 5, 7]
# Bubble Sort
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # swap
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Sorted numbers:", numbers)

#9.Remove duplicates from a list

numbers = [1, 2, 2, 3, 4, 4, 5, 1]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("list after removing duplicate: ",unique_numbers)

#10.Find second largest number in list

numbers = [10,35,67,89,90,100,101]
largest = max(numbers)
while largest in numbers:
    numbers.remove(largest)
second_largest = max(numbers)   
print("Second largest no. in list: ",second_largest) 

#11.Merge and sort two lists

list1 = [4, 1, 9]
list2 = [2, 6, 3]
merged_list = list1 + list2        # Merge both lists
merged_list.sort()                 # Sort the merged list
print("Merged and Sorted List:", merged_list)
