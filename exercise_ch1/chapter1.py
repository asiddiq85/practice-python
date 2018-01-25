# Problem number 1
# find the average of all elements in a list


def average(number_list):
    addition = 0
    for number in number_list:
        addition += number
    return addition/float(len(number_list))


# Problems # 5: Find the 2nd largest number in a list


def second_largest(number_list):
    """we will do a bubble sort on the list and then get the 2nd element to the last"""
    for i in range(len(number_list)):
        for j in range(len(number_list) - 1 - i):
            if number_list[j] > number_list[j+1]:
                number_list[j + 1], number_list[j] = number_list[j],  number_list[j+1]

    return number_list[-2]


# swapping 2 variables

def swap(a, b):
    print("starting with a as: ", a)
    temp = a
    a = b
    b = temp
    return b, a


# 10: reverse a list in place

def reverse_list(numbers):
    i = 0
    j = len(numbers) - 1

    while i < j:
        numbers[i], numbers[j] = numbers[j], numbers[i]
        i += 1
        j -= 1
    return numbers

# Problem 11: Given a set of 0s and 1s. We need to sort the 0s and 1s together so that the 0s are before the 1s.


def zeros_before_ones(zeros_and_ones):
    """slick solution in python ONLY

    zeros = [0 for i in range(zeros_and_ones.count(0))]
    ones = [1 for j in range(zeros_and_ones.count(1))]

    return zeros + ones
    """
    index_i = 0
    last_index = len(zeros_and_ones) - 1

    while index_i < last_index:
        if zeros_and_ones[index_i] == 1 and zeros_and_ones[last_index] == 0:
            zeros_and_ones[index_i], zeros_and_ones[last_index] = zeros_and_ones[last_index], zeros_and_ones[index_i]
        index_i += 1
        last_index -= 1
    # print(zeros_and_ones)
    # TODO: NEEDS IMPROVEMENTS! zeros_and_ones


# Problem # 13. Find the duplicate in a list

def get_duplicate(things):
    """implement with 2 loops :: O(n^2)"""

    for i in range(len(things)):
        for j in range(1, len(things) - 1 - i):
            if things[i] == things[j]:
                print(things[i])

get_duplicate([1, 1, 2, 4, 2])


# Problem number 16
# find the sum of all of the digits in a number
def add_digits_of_number(number):
    s = 0
    while number//10 != 0:
        s += number % 10
        number = number//10
    s += number
    return s


# Problem 15: given a list of numbers and a number, x. find 2 numbers in the list that add up to x.

def find_two_num(numbers, x):
    for number in numbers:
        if x - number in numbers:
            return number, x-number


def find_two_num_2(numbers, x):
    numbers = bubble_sort_list(numbers)
    print("sorted list is: {}".format(numbers))
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[i] > x:
                print("{} > {}".format(numbers[i], x))
                return None
            if numbers[i] + numbers[j] == x:
                return numbers[i], numbers[j]


def bubble_sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers
print(bubble_sort_list([1, 4, 3, 2, 99, 33, 3333, 9389248]))




print(find_two_num([1, 2, 3, 4, 5, 6], 2))
print(find_two_num_2([3, 4, 21, 0, 31, 6, 44, 29, 292], 2))
print(find_two_num_2([1, 2, 3, 4, 5, 6], 2))

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
# f(3,[3,2,1])
f(3)