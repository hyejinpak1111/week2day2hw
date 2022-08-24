#Exercise 1
#Given a list as a parameter,write a function that returns a list of numbers that are less than ten
#For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]

input_list = [1,11,14,5,8,9] #original

def under_ten(input):
    output_list = []
    for i in input: # to read a list, string
        if i < 10:
            output_list.append(i) 
    return output_list

print(under_ten(input_list))

# print(output_list)



#Exercise 2
#Write a function that takes in two lists and returns the two lists merged together and sorted
#Hint: You can use the .sort() method

list_1 = [1,2,3,4,5,6]
list_2 = [3,4,5,6,7,8,10]

def merge_sort(list_a, list_b):
    list_c = list_a + list_b
    list_c.sort()
    return list_c

print(merge_sort(list_1,list_2))

#print(list_3) or print(list_1 | list_2)

# Write a function that takes in a name and prints it with a title.
# E.g., name = 'Wick', title = 'Mr.', output = 'Mr. Wick'

name = 'Wick'
title = 'Mr.'

def merge_name(name, title):
    simp_name = title + ' ' + name
    return simp_name

print(merge_name('Wick', 'Mr.'))
