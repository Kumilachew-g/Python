print("Triangle area with python")

def area_triangle(length, width):
    area = length * width
    return area
area = area_triangle(5, 6)
print("The area of the rectangle is: ", area)

print("Triangle area with python more...")

def area_rectangle(length, width):
    return length * width
area = area_rectangle(5, 6)
print("Area of the rectangle:", area)


print("Even or Odd function with python")

def even_or_odd(number):
    if number % 2 ==0:
        return "Even"
    else:
        return "Odd"
num = 8
result =even_or_odd(num)
print(f"The number {num} is {result}")
# f is used to format the result. The output will beThe number {num} is {result} in python without f key word
print("Even or Odd function with python more...")

def even_or_odd(number):
    return "Even" if num % 2 ==0 else "Odd"
num = 7
result = even_or_odd(num)
print(f"The number {num} is {result}")

#  3 Leap year check
def is_leap_year(year):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 4 Factorial using python function

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

# Example 1
print(factorial(5))  # Output: 120

# Example 2
print(factorial(0))  # Output: 1

# Example 3
print(factorial(10))  # Output: 3628800