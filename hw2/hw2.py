# Name:
# Section:
# hw2.py
import math
from random import randint
##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 ********** 

# def f1(x):
    # print x + 1
# 
# def f2(x):
    # return x + 1
def rock_paper_scissors(player):
	opt = ["Rock", "Paper", "Scissors"]
	opponent = opt[randint(0,2)]
	if player == opponent:
		return "Tie!"
	elif player == "Rock":
		if opponent == "Paper":
			return "You lose!"
		else:
			return "You win!"
	elif player == "Paper":
		if opponent == "Scissors":
			return "You lose!"
		else:
			return "You win!"
	elif player == "Scissors":
		if opponent == "Rock":
			return "You lose!"
		else:
			return "You win!"
print (rock_paper_scissors("Rock"))


# **********  Exercise 2.1 ********** 


# Test Cases for Exercise 2.1
##### YOUR CODE HERE #####

# ********** Exercise 2.2 ********** 

def is_divisible(m, n):
	if m % n == 0:
		return True
	else:
		return False


# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
#print is_divisible(42, 0)  #zero division error


# Define not_equal function here
##### YOUR CODE HERE #####

# Test cases for not_equal
##### YOUR CODE HERE #####

# ********** Exercise 2.3 ********** 

def multadd(a, b, c):
	return a*b+c
# print (multadd(.5, math.cos(math.pi()/4), math.sin(math.pi()/4)))

## 2 - Equations
def multadd(a, b, c):
	return a*b+c
print (multadd(.5, math.cos(math.pi/4), math.sin(math.pi/4)))




# Test Cases
# angle_test =
# print "sin(pi/4) + cos(pi/4)/2 is:"
# print angle_test

# ceiling_test =
# print "ceiling(276/19) + 2 log_7(12) is:"
# print ceiling_test

## 3 - yikes function
def yikes(x):
	e_neg_x = math.e**(-x)
	return multadd(x,e_neg_x, math.sqrt(multadd(-1, e_neg_x, 1)))
print(yikes(5))

# Test Cases
# x = 5
# print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
def rand_divis_3():
	n = randint(0, 100)
	if n % 3 == 0:
		return (True)
	else:
		return (False)
print (rand_divis_3())

# Test Cases
##### YOUR CODE HERE #####

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
def roll_dice(sides, dice):
	for i in range(dice):
		rand_side = randint(0, sides)
		print (rand_side)
	return "That's all!"
print(roll_dice(6, 3))


# Test Cases
##### YOUR CODE HERE #####                            


# ********** Exercise 2.5 **********

# code for roots function
def roots(a, b, c):
	discrim = b**2-4*a*c
	if discrim < 0:
		return "error complex bofa"
	return ((((-b)+(math.sqrt(discrim)))/2*a)), ((((-b)-(math.sqrt(discrim)))/2*a))
print (roots(142, 145, 12))


# Test Cases
##### YOUR CODE HERE #####   
