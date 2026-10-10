# # QUESTION 16

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# remainder = a % b
# print("Remainder =", remainder)

# base = int(input("Enter base: "))
# exp = int(input("Enter exponent: "))

# # QUESTION 17

# result = 1
# for i in range(exp):
#     result = result * base

# print("Power =", result)

# QUESTION 18

# weight = float(input("Enter weight (kg): "))
# height = float(input("Enter height (m): "))

# bmi = weight / (height * height)
# print("BMI =", bmi)

# #  QUESTION 19

# p = float(input("Loan Amount: "))
# r = float(input("Annual Interest Rate (%): "))
# t = int(input("Time (Years): "))

# r = r / (12 * 100)
# n = t * 12

# emi = (p * r * (1 + r) ** n) / ((1 + r) ** n - 1)
# print("Monthly EMI =", emi)

# # QUESTION 20

# s1 = float(input("Subject 1: "))
# s2 = float(input("Subject 2: "))
# s3 = float(input("Subject 3: "))
# s4 = float(input("Subject 4: "))
# s5 = float(input("Subject 5: "))

# total = s1 + s2 + s3 + s4 + s5
# percentage = total / 5

# print("Percentage =", percentage, "%")

# # QUESTION 21

# n = int(input("Enter a number: "))

# if n >= 0:
#     print("Positive")
# else:
#     print("Negative")

# # QUESTION 22

#     n = int(input("Enter a number: "))

# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # QUESTION 23

#     n = int(input("Enter a number: "))

# if n % 5 == 0:
#     print("Divisible by 5")
# else:
#     print("Not Divisible by 5")

# # QUESTION 24

#     year = int(input("Enter year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# # QUESTION 25

#     a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > b:
#     print("Largest =", a)
# else:
#     print("Largest =", b)

# # QUESTION 26

#     a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest =", a)
# elif b >= a and b >= c:
#     print("Largest =", b)
# else:
#     print("Largest =", c)

# # QUESTION 27

#     ch = input("Enter a character: ")

# if ch in "aeiouAEIOU":
#     print("Vowel")
# else:
#     print("Consonant")

# # QUESTION 28

#ch = input("Enter a character: ")

# if ch.isupper():
#     print("Uppercase")
# elif ch.islower():
#     print("Lowercase")
# elif ch.isdigit():
#     print("Digit")
# else:
#     print("Special Character")

# QUESTION 29

#     num = int(input("Enter number: "))
# start = int(input("Enter start of range: "))
# end = int(input("Enter end of range: "))

# if start <= num <= end:
#     print("Number is in range")
# else:
#     print("Number is out of range")

# # QUESTION 30

#    n = int(input("Enter a number: "))

# if n <= 1:
#     print("Not Prime")
# else:
#     prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#             break

#     if prime:
#         print("Prime Number")
#     else:
#         print("Not Prime") 