numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# You are going to write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared.
squared_numbers = [num*num for num in numbers]
print(squared_numbers)

# You are going to write a List Comprehension to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
result = [n for n in numbers if n % 2 == 0]
print(result)

# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.


with open("file1.txt") as file:
    file1 = file.readlines()
file1 = [int(num.strip('\n')) for num in file1]


with open("file2.txt") as file:
    file2 = file.readlines()
file2 = [int(num.strip('\n')) for num in file2]


result = [num for num in file1 if num in file2]
print(result)

# You are going to use Dictionary Comprehension to create a dictionary called
# result that takes each word in the given sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
worlds_list = sentence.split()
result = {world: len(world) for world in worlds_list}
print(result)

# You are going to use Dictionary Comprehension to create a dictionary
# called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp*9/5)+32 for (day, temp) in weather_c.items()}
print(weather_f)


