#!/usr/bin/python
# -*- coding: UTF-8 -*-
current_x = 0.5  # the algorithm starts at x=0.5
learning_rate = 0.001  # step size multiplier
num_iterations = 600000  # the number of times to train the function


# the derivative of the error function (x**4 = the power of 4 or x^4)
def slope_at_given_x_value(x):
    return 5 * x ** 4 - 6 * x ** 2


# Move X to the right or left depending on the slope of the error function
for i in range(num_iterations):
    previous_x = current_x
    current_x += -learning_rate * slope_at_given_x_value(previous_x)
    print(previous_x)

print("The local minimum occurs at %f" % current_x)


def print_error(x):
    temp = x ** 5 - 2 * x ** 3 - 2
    print (temp)


print_error(1.092837)
print_error(1.092218)
print_error(1.095445)
