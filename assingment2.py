import math
import random
import string

# Task 1: List Manipulation with L = [11, 12, 13, 14]
L = [11, 12, 13, 14]

# (i) Add 50 and 60 to L
L.extend([50, 60])

# (ii) Remove 11 and 13 from L
L.remove(11)
L.remove(13)

# (iii) Sort L in ascending order
L.sort()

# (iv) Sort L in descending order
L.sort(reverse=True)

# (v) Search for 13 in L
found = 13 in L

# (vi) Count the number of elements in L
count = len(L)

# (vii) Sum all elements in L
total = sum(L)

# (viii) Sum all even numbers in L
sum_even = sum(x for x in L if x % 2 == 0)

# (ix) Sum all odd numbers in L
sum_odd = sum(x for x in L if x % 2 != 0)

# (x) Sum all prime numbers in L
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sum_primes = sum(x for x in L if is_prime(x))

# (xi) Clear all elements in L
L.clear()

# (xii) Delete L
del L

# Task 2: Sum all items in a list without using sum()
def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

print(sum_list([1, 2, 3, 4]))  # Example usage

# Task 3: Multiply all items in a list without using prod()
def multiply_list(lst):
    result = 1
    for item in lst:
        result *= item
    return result

print(multiply_list([1, 2, 3, 4]))  # Example usage

# Task 4: Create a 3x4x6 3D array filled with *
array_3d = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
print(array_3d)

# Task 5: Dictionary Manipulation with D = {1.5: 6, 2.7: 3.6, 4.8: 7, 5.7: 7}
D = {1.5: 6, 2.7: 3.6, 4.8: 7, 5.7: 7}

# (i) Add new entry (8, 8.8)
D[8] = 8.8

# (ii) Remove key 2.7
D.pop(2.7, None)

# (iii) Check whether 6 is present in D
is_six_present = 6 in D

# (iv) Count the number of elements in D
element_count = len(D)

# (v) Add all values present in D
total_values = sum(D.values())

# (vi) Update the value of 3 to 7.1 (assuming 3 is a key)
D[3] = 7.1

# (vii) Clear the dictionary
D.clear()

# Task 6: Set Manipulation with S1 = {10, 20, 30, 40, 50, 60}, S2 = {40, 50, 60, 70, 80, 90}
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# (i) Add 55 and 66 to S1
S1.update([55, 66])

# (ii) Remove 10 and 30 from S1
S1.discard(10)
S1.discard(30)

# (iii) Check whether 40 is present in S1
is_40_in_S1 = 40 in S1

# (iv) Union of S1 and S2
union_set = S1 | S2

# (v) Intersection of S1 and S2
intersection_set = S1 & S2

# (vi) Find S1 - S2
difference_set = S1 - S2

# Task 7: String and Number Related Programs
# (i) Print 100 random strings of length between 6 and 8
random_strings = [''.join(random.choices(string.ascii_letters, k=random.randint(6, 8))) for _ in range(100)]
print(random_strings)

# (ii) Print all prime numbers between 600 and 800
primes_600_800 = [x for x in range(600, 801) if is_prime(x)]
print(primes_600_800)

# Task 8: Display Examination Schedule
exam_st_date = (11, 12, 2014)
print(f"The examination will start from: {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")

# Task 9: Iterate List and Print Divisible by 5
lst = [10, 20, 33, 46, 55]
div_by_5 = [x for x in lst if x % 5 == 0]
print(div_by_5)

# Task 10: Check if a Number is Even or Odd
def is_even(n):
    return n % 2 == 0

print(is_even(10))  # Example usage

# Task 11: Count Occurrences of 'Emma' in a String
def count_emma(s):
    return s.lower().count("emma")

print(count_emma("Emma is a good girl. Emma loves programming."))  # Example usage

# Task 12: Add Even and Odd Numbers Separately
def add_even_odd(lst):
    even_sum = sum(x for x in lst if x % 2 == 0)
    odd_sum = sum(x for x in lst if x % 2 != 0)
    new_lst = lst + [even_sum] + [odd_sum]
    return new_lst

print(add_even_odd([1, 2, 3, 4, 5]))  # Example usage
