# int
x = 6
y = int(7)
print(type(x))
print(isinstance(x, int))

#float
gpa = 5.5
print(type(gpa))
print(isinstance(gpa, float))


#casting a string to an integer
z ="1234"
z_value = int(z)
print(type(z_value))

# string
name = "hello"
print(type(name))
print(isinstance(name, str))

# bool
is_active = True
print(type(is_active))
print(isinstance(is_active, bool))

# list
nums = [1, 2, 3]
print(type(nums))
print(isinstance(nums, list))

# dictionary
person = {"name": "Alice", "age": 30}
print(person["name"])
print(person["age"])
print(isinstance(person, dict))

# set
unique_numbers = {1, 2, 2, 3}
print(type(unique_numbers))
print(isinstance(unique_numbers, set))

# complex
c = complex(2, 3)
print(type(c))
print(isinstance(c, complex))

# NoneType
nothing = None
print(type(nothing))
print(nothing is None)

# bytes
data = b"hello"
print(type(data))
print(isinstance(data, bytes))