#Exercise 12 – Collections

Objectives:

* To understand the syntax of lists, tuples and dictionaries

Question 1:

1. Create a new PyCharm project: Exercise12.
2. Create a new python file in the project for each of the following questions.
What is wrong with this?

`cheese = ['Cheddar', 'Stilton', 'Cornish Yarg'] 
cheese += 'Oke'`

How should 'Oke' be added to the end of the cheese list?
How would you add two new cheeses to the list with a single command?

Question 2:

What is going on here? Can you explain the output? 

`tup = 'Hello' 
print(len(tup))`

Prints 5 

`tup = 'Hello', 
print(len(tup))`

Prints 1

Question 3:

Write a Python script called lotto.py that will generate and display 6 unique random lottery numbers between 1 and 50. Think about which Python data structure is best suited to store the numbers. Use the Python help() function to find out which function to use from the python standard library called random.