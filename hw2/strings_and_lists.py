# Name:
# Section:
# strings_and_lists.py
import random
# **********  Exercise 2.7 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
    better_list = []
    sum = 0
    for elem in number_list:
        sum += elem
        better_list.append(sum)
    return better_list
print (cumulative_sum([1, 2, 3, 4]))


# Test Cases
##### YOUR CODE HERE #####

# **********  Exercise 2.8 **********

def report_card():
    classes = int(raw_input("How many classes boi?: "))
    grades = []
    class_names = []
    for i in range(classes):
        grade = float(raw_input("what was ur grade?: "))
        class_name = raw_input("what was the class name?: ")
        print (grade)
        print (class_name)
        grades.append(grade)
        class_names.append(class_name)
    gpa = (sum(grades)) / (len(grades))
    print (gpa, grades, class_names)
    print ("Report Card:")
    e = []
    for i in range(classes):
        print (class_names[i] + " " + str(grades[i]))
    print ("Overall GPA " + str(gpa))
report_card()
# Test Cases
## In comments, show the output of one run of your function.

# **********  Exercise 2.9 **********

# Write any helper functions you need here.

def pig_latin(word):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    first_letter = word[0]
    if first_letter in VOWELS:
        word += "hay"
    else:
        word = word[1:] + word[0] + "ay"
    return word
print (pig_latin("ant"))
    ##### YOUR CODE HERE #####
    # return "Not Implemented Yet"    

# Test Cases
##### YOUR CODE HERE #####

import random
# **********  Exercise 2.10 **********
# Test Cases
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for numb in a:
    b.append(numb**3)
print (b)

outputs =[]
flip = random.randint(1,2)
if flip == 1:
    outputs.append("h")
if flip == 2:
    outputs.append("t")
flip_2 = random.randint(1,2)
if flip_2 == 1:
    outputs.append("h")
if flip_2 == 2:
    outputs.append("t")
outputs = ''.join(outputs)
print (outputs)

def vowel_taker(word):
    word_list = list(word)
    vowels = ["a", "e", "i", "o", "u"]
    for letter in word_list:
        if letter in vowels:
            word = word.replace(letter, '')
    return word
print (vowel_taker("hello"))


# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 
