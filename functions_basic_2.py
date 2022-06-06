# question 1
# countdown takes input, and counts down from that input until 0
# ex: 10, will print from 10-0
def countdown(num):
    for i in range(num, -1, -1):
        print(i)
countdown(10)

# question 2
# print_return takes an input of a list with 2 variables and prints the first variable, and returns the second
def print_return(list):
    print(list[0])
    return list[1]
x = print_return([3, 5])
print(x)

# question 3
# first_plus_length accepts a list and returns the sum of the first value and the length of the list
def first_plus_length(list):
    return list[0] + len(list)

x = first_plus_length([1, 5, 7, 8, 9])
print(x)

# question 4
# values_greater_second accepts a list and creates a new list with only variables from the original list that are greater than its second value. Then, returns the list. if there are less than 2 values in the list, return false
def values_greater_second(list):
    new_list = []
    if len(list) < 2:
        return False
    else:
        for i in list:
            if i > list[1]:
                new_list.append(i)
        return new_list

x = values_greater_second([3, 2, 1, -1, 15, 9])
print(x)
x = values_greater_second([15])
print(x)

# question 5
# length_value accepts two integers (size and value). creates and returns a list whos length is equal to the given size, and values are all the given value
def length_value(size, value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list

x = length_value(10, 6)
print(x)
