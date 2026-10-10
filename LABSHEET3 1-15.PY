
# # Question 1: Check if a string is a palindrome.
# text = input("Q1 - Enter a string: ")
# cleaned = text.lower().replace(" ", "")
# if cleaned == cleaned[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# # Question 2: Count the number of vowels and consonants in a string.
# text = input("\nQ2 - Enter a string: ")
# vowels = "aeiouAEIOU"
# vowel_count = consonant_count = 0
# for ch in text:
#     if ch.isalpha():
#         if ch in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
# print("Vowels:", vowel_count)
# print("Consonants:", consonant_count)

# # Question 3: Replace all spaces in a string with underscores.
# text = input("\nQ3 - Enter a string: ")
# result = ""
# for ch in text:
#     if ch == " ":
#         result += "_"
#     else:
#         result += ch
# print("Result:", result)

# # Question 4: Extract all uppercase characters from a string.
# text = input("\nQ4 - Enter a string: ")
# result = ""
# for ch in text:
#     if ch.isupper():
#         result += ch
# print("Uppercase characters:", result)

# # Question 5: Remove all duplicate characters from a string (keep first occurrence).
# text = input("\nQ5 - Enter a string: ")
# result = ""
# for ch in text:
#     if ch not in result:
#         result += ch
# print("Without duplicate characters:", result)

# # Question 6: Find the frequency of each character in a string.
# text = input("\nQ6 - Enter a string: ")
# seen = ""
# for ch in text:
#     if ch not in seen:
#         count = 0
#         for other in text:
#             if other == ch:
#                 count += 1
#         print(repr(ch), ":", count)
#         seen += ch

# # Question 7: Reverse a string without using slicing.
# text = input("\nQ7 - Enter a string: ")
# reversed_text = ""
# index = len(text) - 1
# while index >= 0:
#     reversed_text += text[index]
#     index -= 1
# print("Reversed string:", reversed_text)

# # Question 8: Convert a string into title case without using title().
# text = input("\nQ8 - Enter a string: ")
# result = ""
# new_word = True
# for ch in text:
#     if ch.isspace():
#         result += ch
#         new_word = True
#     elif new_word:
#         result += ch.upper()
#         new_word = False
#     else:
#         result += ch.lower()
# print("Title case:", result)

# # Question 9: Count the number of words in a string.
# text = input("\nQ9 - Enter a sentence: ")
# words = text.split()
# print("Number of words:", len(words))

# # Question 10: Find the longest word in a string.
# text = input("\nQ10 - Enter a sentence: ")
# words = text.split()
# if not words:
#     print("No words entered.")
# else:
#     longest = words[0]
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     print("Longest word:", longest)

# # Question 11: Check if two strings are anagrams of each other.
# first = input("\nQ11 - Enter the first string: ").lower().replace(" ", "")
# second = input("Q11 - Enter the second string: ").lower().replace(" ", "")
# if len(first) != len(second):
#     print("Not anagrams")
# else:
#     remaining = list(second)
#     is_anagram = True
#     for ch in first:
#         if ch in remaining:
#             remaining.remove(ch)
#         else:
#             is_anagram = False
#             break
#     print("Anagrams" if is_anagram else "Not anagrams")

# # Question 12: Check if a substring exists in a given string.
# text = input("\nQ12 - Enter the main string: ")
# substring = input("Q12 - Enter the substring to search: ")
# if substring in text:
#     print("Substring exists")
# else:
#     print("Substring does not exist")

# # Question 13: Convert vowels to uppercase and consonants to lowercase.
# text = input("\nQ13 - Enter a string: ")
# vowels = "aeiouAEIOU"
# result = ""
# for ch in text:
#     if ch in vowels:
#         result += ch.upper()
#     elif ch.isalpha():
#         result += ch.lower()
#     else:
#         result += ch
# print("Converted string:", result)

# # Question 14: Remove all punctuation from a string.
# # import string
# # text = input("\nQ14 - Enter a string: ")
# # result = ""
# # for ch in text:
# #     if ch not in string.punctuation:
# #         result += ch
# # print("Without punctuation:", result)

# # Question 15: Find the first non-repeated character in a string.
# # text = input("\nQ15 - Enter a string: ")
# # first_unique = None
# # for ch in text:
# #     count = 0
# #     for other in text:
# #         if ch == other:
# #             count += 1
# #     if count == 1:
# #         first_unique = ch
# #         break
# # if first_unique is None:
# #     print("No non-repeated character found.")
# # else:
# #     print("First non-repeated character:", first_unique)
