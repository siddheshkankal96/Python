# LIST Questions
# 1. Given a list of numbers, write a Python program to find the sum of all the
# elements in the list.?

from email import header
from operator import concat
from tkinter import N


arr = [1,2,3,4,5]
def find_sum_all_elements(arr):
    return sum(arr)

# print(find_sum_all_elements(arr))
# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# 15

def find_sum_all_elements1(arr):
    total = 0
    for i in arr:
        total += i
    return total

# print(find_sum_all_elements1(arr))

# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# 15


i = 1
j = 3
arr = [2,4,5,10]
def find_sum_all_elements2(arr,i,j):
    total = 0
    for i in range(i,j + 1):
        total += arr[i]
    print(total)

# find_sum_all_elements2(arr,i,j)
# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# 19
# Input: arr = [2,4,5,10], i = 1, j = 3
# Output: 19


# 2. Given an array of integers arr[] of size N and an integer, the task is to
# rotate the array elements to the left by d positions.?

def rorate_array(arr,d):
    rotate = [arr[i] for i in range(d,len(arr)-1)]
    # for i in range(d,len(arr)-1):
    #     rotate.append(arr[i])
    for i in range(d):
        rotate.append(arr[i])    
    for i in rotate:
        print(i, ' ',end = "")
    

# Input:
# arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3 4 5 6 7 1 2

arr = [1, 2, 3, 4, 5, 6, 7] 
d = 2
# rorate_array(arr,d)
# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# 3  4  5  6  1  2  

# 3. Second most repeated word in a sequence in Python?
# Given a sequence of strings, the task is to find out the second most
# repeated (or frequent) string in the given sequence.


# Input : ["aaa", "bbb", "ccc", "bbb",
# "aaa", "aaa"]
# Output : bbb

arr =  ["aaa","bbb","ccc","bbb","aaa","aaa"]
def Second_most_repeated_word(arr):
    counts = dict()
    for word in arr:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

        counts_sorted = sorted(counts.items(), key=lambda a: a[1])
    # print(counts_sorted)
    return counts_sorted[-2][0]

# print(Second_most_repeated_word(arr))

# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# bbb

# 4. Difference between two lists ?


# Input:
# list1 = [10, 15, 20, 25, 30, 35, 40]
# list2 = [25, 40, 35]
# Output:
# [10, 20, 30, 15]


list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]

# output = []
# for i in list1:
#     if i not in list2:
#         output.append(i)

# print((output))

def diff_lists(l1,l2):
    return [i for i in l1 if i not in l2]

# print(diff_lists(list1,list2))

# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# [10, 15, 20, 30]

# 5. Print all positive numbers from given list using for loop Iterate each
# element in the list using for loop and check if number is greater than or
# equal to 0. If the condition satisfies, then only print the number.?
# # Python program to print positive Numbers in a List

# Input: list1 = [12, -7, 5, 64, -14]
# Output: 12, 5, 64
# Input: list2 = [12, 14, -95, 3]
# Output: [12, 14, 3]

list1 = [12, -7, 5, 64, -14]

def find_positive_numbers(arr):
    return [i for i in arr if i >= 0]

# print(find_positive_numbers(list1))
  
# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# [12, 5, 64]  



# 6. Write a Python program to flatten a given nested list structure.?
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

Original_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

def flatten_list(arr):
    flatten_list = []
    flat_list= []
    for i in arr:
        if type(i) == int:
            flatten_list.append(i)
        else:
            list_of_lists = [sublist for sublist in arr if type(sublist) == list ]
            flat_list = [num for sublist in list_of_lists for num in sublist]
            

    flatten_list.extend(flat_list) 
    print(f'original list :')    
    print(f'{arr}')  
    print(f'flatten list :')     
    print(f'{flatten_list}')
    
# flatten_list(Original_list)


# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# original list :
# [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# flatten list :
# [0, 10, 40, 50, 20, 30, 60, 70, 80, 90, 100, 110, 120]
# PS C:\Users\skankal>

# 7. Given an array and a value, find if there is a triplet in array whose sum is
# equal to the given value. If there is such a triplet present in array, then print
# the triplet and return true. Else return false.?
# Input: array = [12, 3, 4, 1, 6, 9], sum = 24;
# Output: 12, 3, 9
# Explanation: There is a triplet (12, 3 and 9) present
# in the array whose sum is 24.
# Input: array = [1, 2, 3, 4, 5], sum = 9
# Output: 5, 3, 1
# Explanation: There is a triplet (5, 3 and 1) present
# in the array whose sum is 9.

array = [12, 3, 4, 1, 6, 9] 
sum = 24
def find_triplet(arr,sum):
    count = 0
    pairs = []
    for i in range(0,len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                if (arr[i] + arr[j] + arr[k]) == sum:
                    pairs.append((arr[i],arr[j],arr[k]))
                    count += 1
    print(f'number of pairs satisying sum value {sum} are : {count}')
    print(f'triplets are : {pairs}')
    print(f'There is a triplet ({i}, {j} and {k}) present')
    
    
# find_triplet(array,sum)

# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# number of pairs satisying sum value 24 are : 1
# triplets are : [(12, 3, 9)]
# There is a triplet (3, 4 and 5) present
# PS C:\Users\skankal>



# =======================================================================================

# Strings
# 1. Missing characters to make a string Pangram.?
# Basic Questions 3
# Pangram is a sentence containing every letter in the English alphabet.
# Given a string, find all characters that are missing from the string, i.e.,
# the characters that can make the string a Pangram.
# We need to print output in alphabetic order.
# Input : welcome to geeksforgeeks
# Output : abdhijnpquvxyz
# Input : The quick brown fox jumps
# Output : adglvyz

# import string
# # list of chars
# def creating_list_chars():
#     letters = []
#     for i in string.ascii_lowercase:
#         letters.append(i)
#     for j in string.ascii_uppercase:
#         letters.append(j)
#     return letters


Input = 'welcome to geeksforgeeks'
def find_missing_chars(string):
    list_of_chars = []
    for i in range(ord('a'),ord('z')+1):
        # print(chr(i), end = '')
        list_of_chars.append(chr(i))
    # print(list_of_chars)
    missing_chars = []
    for i in string:
        if i in list_of_chars:
            list_of_chars.remove(i)
            
    print(''.join(list_of_chars))         
             
# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# abdhijnpquvxyz


# find_missing_chars(Input)

# for i in range(ord('A'),ord('z')+1):
#         print(chr(i), end = '')    
    
    
# 2. Find total number of non-empty substrings of a string with N characters.?
# Input : str = “abc”
# Output : 6
# Every substring of the given string : “a”, “b”, “c”, “ab”, “bc”, “abc”
# Input : str = “abcd”
# Output : 10
# Every substring of the given string : “a”, “b”, “c”, “d”, “ab”,
# “bc”, “cd”, “abc”, “bcd” and “abcd”

string = "abc"

substrings = [string[i:j] for i in range(len(string))
          for j in range(i + 1, len(string) + 1)]
# print(f'original string is : {string}')
# print(f'substrings  are : {substrings}')
# print(f'number of substrings count : {len(substrings)}')




# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# original string is : abc
# substrings  are : ['a', 'ab', 'abc', 'b', 'bc', 'c']
# number of substrings count : 6
# PS C:\Users\skankal>




# 3. Given a string containing lowercase and uppercase letters. Sort it in such
# a manner that the uppercase and lowercase letters come in an alternate
# manner but in a sorted way.?
# Input : bAwutndekWEdkd
# Output :AbEdWddekkntuw
# Explanation:
# Here we can see that letter ‘A’, ’E’, ’W’ are sorted
# as well as letters “b, d, d, d, e, k, k, n, t, u, w” are sorted
# but both appears alternately in the string as far as possible.
# Input :abbfDDhGFBvdFDGBNDasZVDFjkb
# Output :BaBaDbDbDbDdDfFhFjFkGsGvNVZ




# 4. Write a Python program that accepts a comma separated sequence of words as
# input and prints the unique words in sorted form (alphanumerically). ?
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red




# 5. Write a Python program to count the number of characters (character frequency)
# in a string. ?
# Basic Questions 4
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

String = 'google.com'

# string = set(list(String))
# Result = [{i : String.count(i)} for i in string]
Result = dict()

for i in String:
    if i not in Result:
        Result[i] = 1
    else:
        Result[i] += 1

# print(Result)




# 6. find the frequency of minimum occurring character in a python string ?
# The original string is : iNeuronNet.com
# The minimum of all characters in GeeksforGeeks is : i

# String = 'iNeuronNet.com'

# Result = dict()

# String = String.lower()
# for i in String:
#     if i not in Result:
#         Result[i] = 1
#     else:
#         Result[i] += 1
# min = 1
# print(f'The minimum of all characters in {String} is : ')
# for k,v in Result.items():
#     if v == min:
#         print(k , end = ' ')
        
# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# The minimum of all characters in ineuronnet.com is : 
# i u r t . c m



# 8 Write a program extract all the string characters which have odd number of
# occurrences.
# The original string is : geekforgeeks is best for geeks
# The Odd Frequency Characters are : ['k', 'i', 't', 'g', 'e', 'b']

# String = 'geekforgeeks is best for geeks'

# Result = dict()

# String = String.lower()
# for i in String:
#     if i not in Result:
#         Result[i] = 1
#     else:
#         Result[i] += 1
# min = 1
# print(f'The Odd Frequency Characters are :  ')
# # for k,v in Result.items():
# #     if v % 2 != 0:
# #         print(k , end = ' ')

# Results = [k for k,v in Result.items() if v % 2 != 0]
# print(Results)

# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# The Odd Frequency Characters are :  
# ['g', 'e', 'k', 'i', 'b', 't']
# PS C:\Users\skankal>



# ----------------------------------------------------------------------------------


# Dictionary
# 1. Given an input string and a pattern, check if characters in the input string
# follows the same order as determined by characters present in the pattern.
# Assume there won’t be any duplicate characters in the pattern.?
# Input:
# string = "engineers rock"
# pattern = "er";
# Output: true
# Explanation:
# All 'e' in the input string are before all 'r'.
# Input:
# string = "engineers rock"
# pattern = "gsr";
# Output: false
# Explanation:
# There are one 'r' before 's' in the input string.



# 2. Given a list and dictionary, map each element of list with each item of
# dictionary, forming nested dictionary as value.?
# Input : test_dict = {‘Gfg’ : 4, ‘best’ : 9}, test_list = [8, 2]
# Output : {8: {‘Gfg’: 4}, 2: {‘best’: 9}}
# Explanation : Index-wise key-value pairing from list [8] to dict {‘Gfg’ : 4} and so on.

test_dict = {'Gfg' : 4, 'best' : 9}
test_list = [8, 2]

output = dict()
output = { i : {k:v } for k,v in test_dict.items() for i in test_list} 
 
# print(output) 

# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# {8: {'best': 9}, 2: {'best': 9}}


# 3. Sort Dictionary key and values List ?
# Input : test_dict = {‘c’: [3], ‘b’: [12, 10], ‘a’: [19, 4]}
# Output : {‘a’: [4, 19], ‘b’: [10, 12], ‘c’: [3]}
# Input : test_dict = {‘c’: [10, 34, 3]}
# Output : {‘c’: [3, 10, 34]}
test_dict = {'c': [3], 'b': [12, 10], 'a': [19, 4]}

partially_sorted = (dict(sorted(test_dict.items() , key = lambda a: a[0])))
for i in partially_sorted.values():
    i.sort()
    # print(i)
    
# print(partially_sorted)

# for k,v in partially_sorted.items():
#     v.sort()
#     print(v)


# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# {'a': [4, 19], 'b': [10, 12], 'c': [3]}

# 4. Remove all duplicates words from a given sentence ?
# Input : Python is great and Java is also great
# Output : is also Java Python and great

# ******************** approach 1 ********************
Input =  'Python is great and Java is also great'
input = Input.split(' ')
# print(' '.join(list(set(input))))

# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# and also great is Python Java

# ******************** approach 2 ********************

counts  = dict()

for i in input:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1

# print(counts)

output = [i for i in counts.keys()]
output = ' '.join(output)
# print(output)

# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# Python is great and Java also



# 5. Inversion in nested dictionary?
# Input : 
# Output : {‘b’: {‘a’: {}}, ‘e’: {‘d’: {}}, ‘g’: {‘f’: {}}}
# Explanation : Nested dictionaries inverted as outer dictionary keys and viz-a-vis.

test_dict = {'a' : {'b' : {}}, 'd' : {'e' : {}}, 'f' : {'g' : {}}}
output = { a:{k:b} for k,v in test_dict.items() for a,b in v.items() }
# print('original dict : ')
# print(test_dict)
# print('modified dict : ')
# print(output)


# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# original dict : 
# {'a': {'b': {}}, 'd': {'e': {}}, 'f': {'g': {}}}
# modified dict :
# {'b': {'a': {}}, 'e': {'d': {}}, 'g': {'f': {}}}


# 6. Given an array of n string containing lowercase letters. Find the size of
# largest subset of string which are anagram of each others. An anagram of
# a string is another string that contains same characters, only the order of
# characters can be different. For example, “abcd” and “dabc” are anagram
# of each other.?
# Input:
# ant magenta magnate tan gnamate
# Output: 3
# Explanation
# Anagram strings(1) - ant, tan
# Anagram strings(2) - magenta, magnate,
# gnamate
# Thus, only second subset have largest
# size i.e., 3
# Input:
# cars bikes arcs steer
# Output: 2

# arr = ['abdc']
# arr = ''.join(sorted(arr[0]))
# print(arr)

input = ['ant','magenta','magnate','tan','gnamate']
counts = dict()
for i in range(len(input)):
    input[i] = ''.join(sorted(input[i]))

    if input[i] not in counts:
        counts[input[i]] = 1
    else:
        counts[input[i]] += 1
        
# print(input)        
# print(counts)

max_count = max([i for i in counts.values()])
# print(f'output : {max_count}')


# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# output : 3
# ----------------------------------------------------------------------------------


# Sets

# 1. Given two lists a, b. Check if two lists have at least one element common in
# them.
# Input : a = [1, 2, 3, 4, 5]
# b = [5, 6, 7, 8, 9]
# Output : True
# Input : a=[1, 2, 3, 4, 5]
# b=[6, 7, 8, 9]
# Output : False

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
def check_common_exists(a,b):
    for i in a:
        if i in b:
            return True
        else:
            pass


# print(check_common_exists(a,b))

# 2. Return a new set of identical items from two sets
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
# {40, 50, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
output = set()

for i in set1:
    if i in set2:
        output.add(i)
# output = set1.intersection(set2)
# print(output)

# 3. Maximum and Minimum in a Set without use of inbuild max/min functions?
# Input : set = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
# Output : max is 65
# Input : set = ([4, 12, 10, 9, 4, 13])
# Output : min is 4

set = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
set2 = ([4, 12, 10, 9, 4, 13])
def find_min_max(set):
    min = set[0]
    max = set[0]
    for i in set:
        if i < min:
            min = i 
    for i in set:
        if i > max:
            max = i 

    print(f'set : {set}' )
    print(f'max is {max}')
    print(f'min is {min}')
    
# find_min_max(set)
# find_min_max(set2) 

# set : [8, 16, 24, 1, 25, 3, 10, 65, 55]
# max is 65
# min is 1
# set : [4, 12, 10, 9, 4, 13]
# max is 13
# min is 4 


# 4. Write a Python program to check if a set is a subset of another set
# Input :-
# x: {'mango', 'apple'}
# y: {'mango', 'orange'}
# z: {'mango'}
# output :-
# If x is subset of y
# False
# False
# If y is subset of x
# False
# False
# If y is subset of z
# False
# False
# If z is subset of y
# Basic Questions 7
# True
# True
import inspect
x =  {'mango', 'apple'}
y = {'mango', 'orange'}
z = {'mango'}

def check_issubset(a,b):
    # inspect.signature(check_issubset)
    print(f'If {a} is subset of {b}')
    print(a.issubset(b))

# check_issubset(x,y) 
# check_issubset(y,x) 
# check_issubset(y,z) 
# check_issubset(z,y) 

# 5. Write a Python program to remove the intersection of a 2nd set from the 1st set
# input:-
# Original sets:
# {1, 2, 3, 4, 5}
# {4, 5, 6, 7, 8}
# Output:-
# sn1: {1, 2, 3}
# sn2: {4, 5, 6, 7, 8}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


# print(f'original sets : ')
# print(set1)
# print(set2)

for i in set1.intersection(set2):
    set1.remove(i)

# print(f'output : ')
# print(set1)
# print(set2)


# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# original sets : 
# {1, 2, 3, 4, 5}
# {4, 5, 6, 7, 8}
# output :
# {1, 2, 3}
# {4, 5, 6, 7, 8}



# 6. What is the result of passing a dictionary to a set constructor?

numbers_dict = {1:'one',2:'two',3:'three'}
# a = set(numbers_dict)

# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# Traceback (most recent call last):
#   File "c:\Users\skankal\Desktop\python\Python_Assignment.py", line 542, in <module>
#     a = set(numbers_dict)
# TypeError: 'list' object is not callable


# ----------------------------------------------------------------------------------
# Tuple
# 1. Remove Tuples of Length K ?
# Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2
# Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
# Explanation : (4, 5) of len = 2 is removed.

test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
K = 2
output = []
lengths = dict() 
for i in test_list:
    lengths[i] = len(i)


# print(lengths)
# print(output)
for k,v in lengths.items():
    if v == 2:
        continue
    # print(k)
    output.append(k)
    
# print(f'original list : {test_list}')
# print(f'modified list : {output}')

# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# original list : [(4, 5), (4,), (8, 6, 7), (1,), (3, 4, 6, 7)]
# modified list : [(4,), (8, 6, 7), (1,), (3, 4, 6, 7)]


# 2. Removing duplicates from tuple ?
# The original tuple is : (1, 3, 5, 2, 3, 5, 1, 1, 3)
# The tuple after removing duplicates : (1, 3, 5, 2)

# *************** approach 1 *******************
tuple_duplicates = (1, 3, 5, 2, 3, 5, 1, 1, 3)
# tuple_without_duplicates = set(tuple_duplicates)
# print(tuple_without_duplicates)

# *************** approach 2 *******************

duplicates = dict()
for i in tuple_duplicates:
    if i not in duplicates:
        duplicates[i] = 1
    else:
        duplicates[i] += 1


# print(list(duplicates.keys()))

# 3. Flatten tuple of List to tuple ?
# Input : test_tuple = ([5], [6], [3], [8]) Output : (5, 6, 3, 8)
# Input : test_tuple = ([5, 7, 8]) Output : (5, 7, 8)

test_tuple = ([5], [6], [3], [8])
def flatten_tupple(l):    
    output = []
    for i in l:
        output.append(i[0])
        
    print(tuple(output))

# flatten_tupple(test_tuple)


# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# (5, 6, 3, 8)    




# 4. Remove nested records from tuple?
# The original tuple : (1, 5, 7, (4, 6), 10)
# Elements after removal of nested records : (1, 5, 7, 10)

nested_tuple = (1, 5, 7, (4, 6), 10)
tuple_output = list(filter(lambda a : type(a) == int ,nested_tuple))

# print(tuple_output)


# 5. Convert Binary tuple to Integer?

# The original tuple is : (1, 1, 0, 1, 0, 0, 1)
# Decimal number is : 105
tup = (1, 1, 0, 1, 0, 0, 1)
def conver_binaryToInteger(tup):    
    rev_tup = tup[::-1]
    total = 0
    for index,value in enumerate(rev_tup):
        total += (value * 2**index)
    
    return total

# print(conver_binaryToInteger(tup))


# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# 105


# 6. Sort Tuples by Total digits?
# Input : test_list = [(3, 4, 6, 723), (1, 2), (134, 234, 34)]
# Output : [(1, 2), (3, 4, 6, 723), (134, 234, 34)]
# Explanation : 2 < 6 < 8, sorted by increasing total digits.

test_list = [(3, 4, 6, 723), (1, 2), (134, 234, 34)]
total = []
temp = 0
for i in test_list:
    temp = 0
    for j in i:
        temp += j
    total.append(temp)

test_list_tuples  = tuple()     
# for i in zip(test_list,total):
    # test_list_tuples.

output = [i[0] for i in sorted(tuple(zip(test_list,total)), key = lambda x : x[1])]

# print(output)


# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# [(1, 2), (134, 234, 34), (3, 4, 6, 723)]
# ----------------------------------------------------------------------------------

# MAP & Lambda Function
# 1. Write a Python program to add three given lists using Python map and lambda.?
# Original list:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# New list after adding above three lists:
# [12, 15, 18]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
# print('Original list : ')
# print(list1)
# print(list2)
# print(list3)

# print('New list after adding above three lists: ') 

output = list(map(lambda a,b,c : a + b + c, list1,list2,list3))
# print(output)


# 2. Write a Python program to convert a given list of tuples to a list of strings using
# map function?
# Original list of tuples:
# [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
# Convert the said list of tuples to a list of strings:
# ['red pink', 'white black', 'orange green']

# a= 'a'
# b = 'b'
# print(concat(a,b))

input = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
output = list(map(' '.join,input))
# print(output)


# 3. Write a Python program to add two given lists and find the difference between
# lists. Use map() function?
# Original lists:
# [6, 5, 3, 9]
# [0, 1, 7, 7]
# Result:
# [(6, 6), (6, 4), (10, -4), (16, 2)]


l1 = [6, 5, 3, 9]
l2 = [0, 1, 7, 7]
output = list(zip(tuple(map(lambda x,y : x+y ,l1,l2)),tuple(map(lambda x,y : x-y ,l1,l2))))
# print(output)


# 4. Write a Python program to create Fibonacci series upto n using Lambda?

# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Python code to demonstrate the working of
# sum()


# l = [0,1]
# print(l[-2:])
def sum(l):
    total = 0
    for i in (l[-2:]):
        total += i
    l.append(total)
    # print(l)
  
    
    
def fibonacci(count):
   listA = [0, 1]

   any(map(lambda x : sum(listA),
         range(2, count)))

   return listA[:count]

# print(fibonacci(8))


# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# [0, 1, 1, 2, 3, 5, 8, 13]
# PS C:\Users\skankal>    


# 5. Write a Python program to find intersection of two given arrays using Lambda ?
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]

l1 = [1, 2, 3, 5, 7, 8, 9, 10]
l2 = [1, 2, 4, 8, 9]
# print('arrays are : ')  
# print(l1 , l2)
# print('Intersection of the arrays: ') 
# print(list(filter(lambda a : a in l1,l2)))


# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# arrays are : 
# [1, 2, 3, 5, 7, 8, 9, 10] [1, 2, 4, 8, 9]
# Intersection of the arrays:
# [1, 2, 8, 9]


# 6. Write a Python program to find palindromes in a given list of strings using
# Lambda ?
# Orginal list of strings:
# ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# List of palindromes:
# ['php', 'aaa']

String = 'abc'
reverse = lambda string : string[::-1]
# print(reverse(String))

def find_palindromes(l):
    # return list(filter(lambda string : string == string[::-1],l))
    return list(filter(lambda string : string == reverse(string),l))

# print(find_palindromes(['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']))

# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# ['php', 'aaa']



# 7. Write a Python program to find the list with maximum and minimum length using
# lambda ?
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])



# def max_length_list(input_list):
#     max_length = max(len(x) for x in input_list )   
#     max_list = max(input_list, key = lambda i: len(i))    
#     return(max_length, max_list)
    
# def min_length_list(input_list):
#     min_length = min(len(x) for x in input_list )  
#     min_list = min(input_list, key = lambda i: len(i))
#     return(min_length, min_list)
      
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# print("Original list:")
# print(list1)
# print("\nList with maximum length of lists:")
# print(max_length_list(list1))
# print("\nList with minimum length of lists:")
# print(min_length_list(list1))

# ************** approach 2********************
# lengths_of_lists = dict()
# for i in list1:
#     lengths_of_lists[str(i)] = len(i)

# print(lengths_of_lists)
# max_list = max(lengths_of_lists, key = lambda v: len(v))
# min_list = min(lengths_of_lists, key = lambda v: len(v))
# print(f'{max_list} :  {len(max_list)}')
# print(f'{min_list} :  {len(min_list)}')

# ************** approach 3********************
# min_length = min(lengths_of_lists.values())
# min_list = [key for key in lengths_of_lists if lengths_of_lists[key] == min_length]

# max_length = max(lengths_of_lists.values())
# max_list = [key for key in lengths_of_lists if lengths_of_lists[key] == max_length]


# print(min_length , min_list)
# print(max_length,max_list)



# 8. Write a Python program to triple all numbers of a given list of integers.?
# Original list: (1, 2, 3, 4, 5, 6, 7)
# Triple of said list numbers:
# [3, 6, 9, 12, 15, 18, 21]

original_list = [1, 2, 3, 4, 5, 6, 7]
triple = [i * 3 for i in original_list]

# print(f'original_list : {original_list}')
# print(f'triple : {triple}')
# -----------------------------------------------------------------------------------

# List Comprehension
# 1. Use a nested list comprehension to find all of the numbers from 1–1000 that are
# divisible by any single digit besides 1 (2–9)?
l = [i for i in range(1,1001) for j in range(2,10) if i % j == 0 ]
# print(l)

# 2. Use list comprehension to construct a new list but add 6 to each item?
l2 = [i + 6 for i in range(1,11)]
# print(l2)



# 3. Suppose we want to create an output dictionary which contains only the odd
# numbers that are present in the input list as keys and their cubes as values.
# Let’s see how to do this using for loops and dictionary comprehension.?
input = [1, 2, 3, 4, 5, 6, 7]
# outpur :- {1: 1, 3: 27, 5: 125, 7: 343}

dictionary = {i : i**3 for i in input if i % 2 != 0}

# print(dictionary)

# 4. Given two lists containing the names of states and their corresponding capitals,
# construct a dictionary which maps the states with their respective capitals. Let’s
# see how to do this using for loops and dictionary comprehension.?
state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
# output:- {'Gujarat': 'Gandhinagar','Maharashtra': 'Mumbai', 'Rajasthan': 'Jaipur'}

# output = dict()
# for k,v in zip(state,capital):
#     output[k] = v 

output = {k:v for k,v in zip(state,capital)}
# print(output)


# 5. Transpose of Matrix using Comprehension?
# Input :- [[1, 2, 3, 4], [4, 5, 6, 8]]
# Output :- [[1, 4], [2, 5], [3, 6], [4, 8]]


# 6. We have a string ‘2459a09b’ and we want to extract all integer literals, and use
# int() to cast them into integers.?
Input = '2459a09b'
# output :- [2, 4, 5, 9, 9]
# print(type(int(Input[0])))
# output = list(map(int,filter(lambda i : ord(i) >= 49 and ord(i) <= 57,Input)))
output = [int(i) for i in Input if ord(i) >=49 and ord(i) <= 57]
# print(output)


# 7. Finding the elements in a list in which elements are ended with the letter
# ‘b’ and the length of that element is greater than 2?
# input :- names = ['Ch','Dh','Eh','cb','Tb','Td','Chb','Tdb']
# output :- ['Chb', 'Tdb']
names = ['Ch','Dh','Eh','cb','Tb','Td','Chb','Tdb']

output = [name for name in names if name.endswith('b') and len(name) > 2]
# print(output)





# 8. Reverse each String in a Tuple using list comprehension ?
# Input :- 'Hello', 'Analytics', 'Vidhya'
# output :- ['olleH', 'scitylanA', 'ayhdiV']

Input = ('Hello', 'Analytics', 'Vidhya')

output = [word[::-1] for word in Input]

# print(output)


# --------------------------------------------------------------------------------------

# Object Oriented Programming
# 1. Define a property that must have the same value for every class instance
# (object)?
# Output :-
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

class Vehicle:
    # Class variable
    color = "White"
    #constructor
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f'Color: {Vehicle.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}'
    
    


# School_bus = Vehicle("School Volvo", 180, 12)
# car = Vehicle("Audi Q5", 240, 18)

# print(School_bus)
# print(car)

# PS C:\Users\skankal> python -u "c:\Users\skankal\Desktop\python\Python_Assignment.py"
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18


# 2. Create a class with property decorator with setter and getter functions.?

class House:

	def __init__(self, price):
		self._price = price
    

	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self._price
    
       
# house = House(50000.0)
# print(house.price) 

# house.price = 2000.0   
# print(house.price) 


# 3. Create a class with Multi-level Inheritance ?
class Grandparent:
    
    def __init__(self, name, age):
      self.name = name
      self.age = age
    
    def __str__(self):
        return f'name: {self.name}, age: {self.age}'
    
class Parent(Grandparent):
    def __init__(self, name, age):
        super().__init__(name,age)
    
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name,age)
        
child = Grandparent('sandeep',25)
# print(child)
    
# 4. Create a class a overwrite a class Destructor ?

class Student:

    # constructor
    def __init__(self, name):
        self.name = name


    def show(self):
        print(f'Hello, my name is, {self.name}')

    # destructor
    def __del__(self):
        print('The destructor is called for deleting the Student.')

# create object
# s1 = Student('Arnav')
# s1.show()

# delete object
# del s1



# 5. write a decorator for a class?

 
# class MyDecorator:
#     def __init__(self, function):
#         self.function = function
     
#     def __call__(self):
 
#         # We can add some code
#         # before function call
#         print('calling function')
#         self.function()
#         print('function called')
#         # We can also add some code
#         # after function call.
 
 
# # adding class decorator to the function
# @MyDecorator
# def function():
#     print("GeeksforGeeks")
 
# function()

# 6. Implement a stack ?

# implementation using list 
# suppose we have an list stack

stack= []

# stack is working on LIFO principle (last in first out)

# function to add elemnts into stack at last position (push operation)
def push(i):
    stack.append(i)

# function to remeove elemnts into stack at last position (pop operation)
def pop():
    stack.pop()
    
push(2)  
push(4)
push(5)  
push(7) 
# print(stack)
pop() 
# print(stack)
pop() 
# print(stack)


# implementation using class 
class stack:
    def __init__(self,value:list = []):
        self.value = []
        print('stack created')

    def pop(self):
        self.value.pop()
    
    def push(self,i):
        self.value.append(i)
        print(f'{i} pushed into stack')   

    def __iter__(self):
        for i in self.value:
            yield i    

# s1 = stack()
# s1.push(2)
# s1.push(3) 
# s1.push(5)
# s1.push(7) 
# s1.push(2)
# s1.push(7) 
# print([i for i in s1])
# s1.pop()
# s1.pop()
# print([i for i in s1])    

 
# 7. Implement a Queue ?


class Queue:
    def __init__(self,value:list = []):
        self.value = []
        print('Queue created')

    def dequeue(self):
        popped_item = self.value.pop(0)
        print(f'dequeued element : {popped_item}')
    
    def enqueue(self,i):
        self.value.append(i)
        print(f'{i} added into Queue')   

    def __iter__(self):
        for i in self.value:
            yield i   
            
            
# q1 = Queue()
# q1.enqueue(2)
# q1.enqueue(3) 
# q1.enqueue(5)
# q1.enqueue(7) 
# q1.enqueue(2)
# q1.enqueue(7) 
# q1.enqueue(7) 
# print([i for i in q1])
# q1.dequeue()
# q1.dequeue()
# # print([i for i in q1])  

# 8. Implement a Linked List ?

##******************** implementation of singly-linked-list ********************

class node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
    def insertNodeInSLL(self,value,location):
        newnode = node(value)
        
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:
                newnode.next = self.head
                self.head = newnode
                
            elif location == 1:
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            
            else:
                tempnode = self.head
                index = 0
                
                while index < location-1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                
                tempnode.next = newnode
                newnode.next = nextnode

#*************************  traversal through singly linked list #*************************

    def traversalSLL(self):
        if self.head is None:
            print("singly linked list is empty")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
                        
        

            

singlylinkedlist = SinglyLinkedList()

# node1 = node(1)
# node2 = node(2)

# singlylinkedlist.head = node1
# singlylinkedlist.head.next = node2
# singlylinkedlist.tail = node2

singlylinkedlist.insertNodeInSLL(1,0)
singlylinkedlist.insertNodeInSLL(2,0)
singlylinkedlist.insertNodeInSLL(3,1)
singlylinkedlist.insertNodeInSLL(4,2)
singlylinkedlist.insertNodeInSLL(5,2)
# singlylinkedlist.traversalSLL()

# print([node.value for node in singlylinkedlist])  




# 9. Explain What happens you create a object of a class (Inside python)?

class student:
    def __init__(self):
        print("object created and constructor is called")
    
# s1 = student()

# conclusion is whenever object is created first constructor is called by default

# 10. Create a class whose object should be called like a function.?
# class Product:
# def __init__(self):
# print("Instance Created")
# # Instance created
# ans = Product()
# ans(10, 20) -> should return product

class Product:
    def __init__(self):
        print("Instance Created")
    def __call__(self,a:int,b:int):
        print(a*b)


# ans = Product()
# ans(10, 20) 

# Exception Handling
# 1. Write Custom Exception to handle Zero division Error ?

# **********************approach 1 system defined excpetion handler **********************
# try:
#     num1 = int(input("Enter First Number: "))
#     num2 = int(input("Enter Second Number: "))

#     result = num1 / num2

#     print(result)
# except ValueError as e:
#     print("Invalid Input Please Input Integer...")
# except ZeroDivisionError as e:
#     print(e)
    


# ******************approach 2 through base class **************************

# class Error(Exception):
#     """Base class for other exceptions"""
#     pass


# class Zero_division_Error(Error):
#     """Raised when the input value zero for second input"""
#     pass

# try:
#     num1 = input("Enter First Number: ")
#     num2 = input("Enter Second Number: ")
#     if num2 == 0:
#         raise Zero_division_Error
#     result = num1 / num2
#     print(result)
# except Zero_division_Error:
#     print("Invalid Input Please Input value greater than 0 for second number...")



# ******************approach 3 using  Customizing Exception Classes **************************
# class Zero_division_Error(Exception):
#     """Exception raised for  Zero_division_Error. """
    
#     def __init__(self, message="Salary is not in (5000, 15000) range"):
#         self.message = message
#         super().__init__(self.message)

#     def __str__(self):
#         return f'Error message -> {self.message}'


# num1 = input("Enter First Number: ")
# num2 = input("Enter Second Number: ")
# if num2 == 0:
#     raise Zero_division_Error
# else:
#     result = num1 / num2
#     print(result)



# 2. Catching specific exception in Python.?
# try:
#     num1 = int(input("Enter First Number: "))
#     num2 = int(input("Enter Second Number: "))

#     result = num1 / num2

#     print(result)
# except ValueError as e:
#     print("Invalid Input Please Input Integer...")
# except ZeroDivisionError as e:
#     print(e)


