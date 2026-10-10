
# # Q16. Count digits, alphabets, and special characters

# s = input("Enter a string: ")
# digits = 0
# alphabets = 0
# special = 0

# for ch in s:
#     if ch.isdigit():
#         digits += 1
#     elif ch.isalpha():
#         alphabets += 1
#     elif not ch.isspace():
#         special += 1

# print("Digits:", digits)
# print("Alphabets:", alphabets)
# print("Special characters:", special)

# # Q17. Print all substrings of a string

# s = input("Enter a string: ")

# for i in range(len(s)):
#     for j in range(i + 1, len(s) + 1):
#         print(s[i:j])

# # Q18. Sort characters alphabetically

# s = input("Enter a string: ")
# print("".join(sorted(s)))

# # Q19. Find the most repeated word in a string

# s = input("Enter a string: ")
# words = s.lower().split()

# if words:
#     most_repeated = max(set(words), key=words.count)
#     print("Most repeated word:", most_repeated)
#     print("Frequency:", words.count(most_repeated))
# else:
#     print("No words found.")

# # Q20. Check if two strings are rotations of each other

# s1 = input("Enter the first string: ")
# s2 = input("Enter the second string: ")

# if len(s1) == len(s2) and s2 in s1 + s1:
#     print("The strings are rotations of each other.")
# else:
#     print("The strings are not rotations of each other.")

# # Q21. Find the largest and smallest elements in a list

# numbers = [12, 5, 27, 3, 18]
# print("Largest:", max(numbers))
# print("Smallest:", min(numbers))

# # Q22. Sort a list in ascending and descending order

# numbers = [12, 5, 27, 3, 18]
# print("Ascending:", sorted(numbers))
# print("Descending:", sorted(numbers, reverse=True))
# # Q23. Remove duplicate elements from a list

# numbers = [10, 20, 10, 30, 20, 40]
# unique_numbers = list(dict.fromkeys(numbers))
# print(unique_numbers)
# # Q24. Reverse a list without using built-in functions

# numbers = [10, 20, 30, 40, 50]
# reversed_numbers = []

# for i in range(len(numbers) - 1, -1, -1):
#     reversed_numbers.append(numbers[i])

# print(reversed_numbers)
# # Q25. Count the frequency of each element in a list

# numbers = [10, 20, 10, 30, 20, 10]

# for item in dict.fromkeys(numbers):
#     print(item, ":", numbers.count(item))

# # Q26. Merge two lists into one

# list1 = [10, 20, 30]
# list2 = [40, 50, 60]
# merged_list = list1 + list2
# print(merged_list)

# # Q27. Find the second largest number in a list

# numbers = [10, 25, 40, 30, 40]
# unique_numbers = sorted(set(numbers))

# if len(unique_numbers) >= 2:
#     print("Second largest:", unique_numbers[-2])
# else:
#     print("There is no second largest number.")

# # Q28. Find common elements in two lists

# list1 = [10, 20, 30, 40]
# list2 = [30, 40, 50, 60]
# common = list(dict.fromkeys(x for x in list1 if x in list2))
# print(common)
# # Q29. Find the difference between two lists

# list1 = [10, 20, 30, 40]
# list2 = [30, 40, 50, 60]
# difference = [x for x in list1 if x not in list2]
# print(difference)
# # Q30. Separate even and odd numbers from a list

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even = [x for x in numbers if x % 2 == 0]
# odd = [x for x in numbers if x % 2 != 0]

# print("Even numbers:", even)
# print("Odd numbers:", odd)
