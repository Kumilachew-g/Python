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