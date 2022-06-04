# Question: Given two strings, write a function to determine whether they are anagrams.

# Clarifications: Definition of anagram.

# Solutions: Convert to lowercase, turn to array, sort, return comparison.

# Complexity: O (nm * log(nm))


def anagram(a, b) -> bool:

    a = a.lower()
    b = b.lower()

    a_arr = []
    for letter in a:
        a_arr.append(letter)
    a_arr.sort()

    b_arr = []
    for letter in b:
        b_arr.append(letter)
    b_arr.sort()

    return a_arr == b_arr

a = "aSdf"
b = "dfsA"
print(anagram(a, b))

a = "asdfa"
b = "dfsA"
print(anagram(a, b))