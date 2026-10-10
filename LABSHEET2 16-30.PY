# # QUESTION 16
# for i in range(1, 51, 2):
#     print(i)
# # QUESTION 17
# n = int(input("Enter a number: "))

# fact = 1

# for i in range(1, n + 1):
#     fact *= i

# print("Factorial:", fact)
# # QUESTION 18
# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
# # QUESTION 19
# n = int(input("Enter a number: "))

# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10

# print("Reverse:", reverse)
# # QUESTION 20
# n = int(input("Enter a number: "))

# count = 0

# if n == 0:
#     count = 1
# else:
#     while n != 0:
#         n //= 10
#         count += 1

# print("Number of digits:", count)
# # QUESTION 21
#  n = int(input("Enter a number: "))

# sum = 0

# while n > 0:
#     digit = n % 10
#     sum += digit
#     n //= 10

# print("Sum of digits:", sum)
# # QUESTION 22
# for n in range(2, 101):
#     count = 0

#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1

#     if count == 2:
#         print(n)
# # QUESTION 23
# n = int(input("Enter a number: "))

# sum = 0

# for i in range(1, n):
#     if n % i == 0:
#         sum += i

# if sum == n:
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")
# # QUESTION 24
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# # QUESTION 25
# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# # QUESTION 26
# n = int(input("Enter number of rows: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end=" ")

#     for j in range(1, i + 1):
#         print(j, end=" ")

#     print()
# # QUESTION 27
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end="\t")
#     print()
# # QUESTION 28
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# hcf = 1

# for i in range(1, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         hcf = i

# print("HCF:", hcf)
# # QUESTION 29
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# lcm = max(a, b)

# while True:
#     if lcm % a == 0 and lcm % b == 0:
#         break
#     lcm += 1

# print("LCM:", lcm)
# # QUESTION 30
# n = int(input("Enter a number: "))

# temp = n
# sum = 0

# while temp > 0:
#     digit = temp % 10

#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i

#     sum += fact
#     temp //= 10

# if sum == n:
#     print("Strong Number")
# else:
#     print("Not a Strong Number")
