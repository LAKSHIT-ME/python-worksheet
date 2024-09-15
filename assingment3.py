import math

# 1. Calculate the difference between a given number and 17
def difference(n):
    if n > 17:
        return 2 * abs(n - 17)
    else:
        return abs(n - 17)

# 2. Test if a number is within 100, 1000, or 2000
def test_number(n):
    return 100 <= n <= 1000 or n == 2000

# 3. Reverse a string
def reverse_string(s):
    return s[::-1]

# 4. Count upper and lower case letters in a string
def count_letters(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

# 5. Return a list with distinct elements
def distinct_elements(lst):
    return list(set(lst))

# 6. Print even numbers from a given list
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# 7. Access a function inside a function
def outer_function():
    def inner_function():
        return "Inner function accessed"
    return inner_function()

# 8. Define a function with attributes and display argument names
def student(name, age):
    pass

student.name = "name"
student.age = "age"

# 9. `Student` class with attributes and a display function
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None  # Added attribute

    def display(self):
        return vars(self)

# 10. `Student` class with instances and attribute printing
class StudentInstances:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

# 11. `Circle` class with area and perimeter methods
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# 12. Class with `get_String` and `print_String` methods
class StringHandler:
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Enter a string: ")

    def print_String(self):
        print(self.string.upper())

# Example usage
print(difference(22))  # Task 1
print(test_number(150))  # Task 2
print(reverse_string("hello"))  # Task 3
print(count_letters("Hello World"))  # Task 4
print(distinct_elements([1, 2, 2, 3, 4, 4]))  # Task 5
print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Task 6
print(outer_function())  # Task 7
print(student.__dict__)  # Task 8

student = Student(1, "John")  # Task 9
student.student_class = "10th Grade"
print(student.display())

student1 = StudentInstances(1, "John")  # Task 10
student2 = StudentInstances(2, "Jane")
print(vars(student1))
print(vars(student2))

circle = Circle(5)  # Task 11
print(circle.area())
print(circle.perimeter())

handler = StringHandler()  # Task 12
# handler.get_String()  # Uncomment for input
# handler.print_String()  # Uncomment for output
