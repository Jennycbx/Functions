# def greet():
#     print("Hey")

# greeting = greet()

# print(greeting)

# def greet(name):
#     return "Hey " + name

# greeting = greet("Bob")
# print(greeting)

def greet(name, time_of_day):
    return "Good " + time_of_day +", " + name

greeting = greet('Bob', 'morning')
print(greeting)