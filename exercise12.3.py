import random

'''numbers_drawn_for = []
for i in range(6): # Only ever runs 6 times.
    n = random.randint(1,51)
    if n not in numbers_drawn_for:
        numbers_drawn_for.append(n) # only appends if n is not in numbers_drawn list'''

numbers_drawn_while = []
while len(numbers_drawn_while) < 6: # Will run until len of numbers_drawn = 6
    n = random.randint(1, 51)
    if n not in numbers_drawn_while:
        numbers_drawn_while.append(n) # only appends if n is not in numbers_drawn
print(numbers_drawn_while)

''' The while loop ensures that 6 numbers are generated each time and that the output always contains 6 numbers. 
After a few tries of the for loop the generator outputted less than 6 numbers. This is because the number already 
existed in the numbers_drawn list.  
'''

