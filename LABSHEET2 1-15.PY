# QUESTION 1

# n = int(input("Enter a number: "))

# if n % 3 == 0 and n % 7 == 0:
#     print("Number is a multiple of both 3 and 7")
# else:
#     print("Number is not a multiple of both 3 and 7")

# QUESTION 2

# n = int(input("Enter a number: "))

# if str(n) == str(n)[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# QUESTION 3
# n = int(input("Enter a number: "))

# temp = n
# digits = len(str(n))
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     sum += digit ** digits
#     temp //= 10

# if sum == n:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")
# QUESTION 4
# marks = int(input("Enter marks: "))

# if marks >= 90 and marks <= 100:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# elif marks >= 0:
#     print("Grade F")
# else:
#     print("Invalid marks")
# QUESTION 5
# n = int(input("Enter a number: "))

# if n < 0:
#     n = -n

# print("Absolute value:", n)
# QUESTION 6  
# a = int(input("Enter first angle: "))
# b = int(input("Enter second angle: "))
# c = int(input("Enter third angle: "))

# if a > 0 and b > 0 and c > 0 and a + b + c == 180:
#     print("Valid Triangle")
# else:
#     print("Invalid Triangle")
# QUESTION 7
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a == b == c:
#     print("Equilateral Triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")
# QUESTION 8
# text = input("Enter a string: ")
# sub = input("Enter substring: ")

# if sub in text:
#     print("Substring found")
# else:
#     print("Substring not found")
# # QUESTION 9
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Eligible for voting")
# else:
#     print("Not eligible for voting")
# QUESTION 10
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a <= b and a <= c:
#     print("Smallest:", a)
# elif b <= a and b <= c:
#     print("Smallest:", b)
# else:
    # print("Smallest:", c)
# QUESTION 11
# for i in range(1, 11):
    # print(i)
# QUESTION 12
# i = 10

# while i >= 1:
    # print(i)
    # i -= 1
# QUESTION 13
# n = int(input("Enter n: "))

# sum = 0

# for i in range(1, n + 1):
    # sum += i

# print("Sum:", sum)

# QUESTION 14

# n = int(input("Enter a number: "))

# for i in range(1, 11):
    # print(n, "x", i, "=", n * i)

# QUESTION 15
# for i in range(2, 51, 2):
#     print(i)