Notebook - User Input
Section 2, Lecture 8

    #User input
    input("Please enter the string you want to be printed out: ")
     
    #Saving the input to a variable
    user_says = input("Please enter the string you want to be printed out: ")
	
Notebook - Variables
Section 2, Lecture 10

    #Defining a variable
    my_var = 10 #type integer
    my_var = "Hello" #type string
    my_var = True #type boolean

Notebook - Strings
Section 3, Lecture 17

    #Defining a string on multiple lines, using triple quotes and the line continuation character ( \ )
    my_string = '''this\
    is\
    my\
    first\
    string'''
     
    #Strings - indexing
    a = "Cisco Switch"
     
    a.index("i")
     
    #Strings - character count
    a = "Cisco Switch"
     
    a.count("i")
     
    #Strings - finding a character
    a = "Cisco Switch"
     
    a.find("sco")
     
    #Strings - converting the case
    a = "Cisco Switch"
     
    a.lower() #lowercase
     
    a.upper() #uppercase
     
    #Strings - checking whether the string starts with a character
    a = "Cisco Switch"
     
    a.startswith("C")
     
    #Strings - checking whether the string ends with a character
    a = "Cisco Switch"
     
    a.endswith("h")
     
    #Strings - removing a character from the beginning and the end of a string
    a = "   Cisco Switch   "
     
    a.strip() #remove whitespaces
     
    b = "$$$Cisco Switch$$$"
     
    b.strip("$") #remove a certain character
     
    #Strings - removing all occurences of a character from a string
    a = "   Cisco Switch   "
     
    a.replace(" ", "") #replace each space character with the absence of any character
     
    #Strings - splitting a string by specifying a delimiter; the result is a list
    a = "Cisco,Juniper,HP,Avaya,Nortel" #the delimiter is a comma
     
    a.split(",")
     
    #Strings - inserting a character in between every two characters of the string / joining the characters by using a delimiter
    a = "Cisco Switch"
     
    "_".join(a)
     
    #Additional methods (source: https://www.tutorialspoint.com/python3/python_strings.htm) 
     
    capitalize()
    #Capitalizes first letter of string.
     
    lstrip()
    #Removes all leading whitespace in string.
     
    rstrip()
    #Removes all trailing whitespace of string.
     
    swapcase()
    #Inverts case for all letters in string.
     
    title()
    #Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.
     
    isalnum()
    #Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.
     
    isalpha()
    #Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
     
    isdigit()
    #Returns true if string contains only digits and false otherwise.
     
    islower()
    #Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.
     
    isnumeric()
    #Returns true if a unicode string contains only numeric characters and false otherwise.
     
    isspace()
    #Returns true if string contains only whitespace characters and false otherwise.
     
    istitle()
    #Returns true if string is properly "titlecased" and false otherwise.
     
    isupper()
    #Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.
     
    #Strings - concatenating two or more strings
    a = "Cisco"
    b = "2691"
     
    a + b
     
    #Strings - repetition / multiplying a string
    a = "Cisco"
     
    a * 3
     
    #Strings - checking if a character is or is not part of a string
    a = "Cisco"
     
    "o" in a
     
    "b" not in a
     
    #Strings - formatting v1
    "Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4)
    "Cisco model: %s, %d WAN slots, IOS %.f" % ("2600XM", 2, 12.4)
    "Cisco model: %s, %d WAN slots, IOS %.1f" % ("2600XM", 2, 12.4)
    "Cisco model: %s, %d WAN slots, IOS %.2f" % ("2600XM", 2, 12.4)
     
    #Strings - formatting v2
    "Cisco model: {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4)
    "Cisco model: {0}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4)
     
    #Strings - slicing
    string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"
     
    string1[5:15] #slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice
    string1[5:] #slice starting at index 5 up to the end of the string
    string1[:10] #slice starting at the beginning of the string up to, but NOT including, index 10
    string1[:] #returns the entire string
    string1[-1] #returns the last character in the string
    string1[-2] #returns the second to last character in the string
    string1[-9:-1] #extracts a certain substring using negative indexes
    string1[-5:] #returns the last 5 characters in the string
    string1[:-5] #returns the string minus its last 5 characters
    string1[::2] #adds a third element called step; skips every second character of the string
    string1[::-1] #returns string1's elements in reverse order

Notebook - Numbers and Math Operators
Section 4, Lecture 19

    #Numbers
    num1 = 10
    num2 = 2.5
     
    type(num1) #checking the type of this variable; integer
    type(num2) #checking the type of this variable; float
     
    #Numbers - math operations
    1 + 2 #addition
     
    2 – 1 #subtraction
     
    4 / 2 #division
     
    4 * 2 #multiplication
     
    4 ** 2 #raising to a power
     
    5 % 2 #modulo (this means finding out the remainder after division of one number by another)
     
    #Numbers - float division vs. integer division (special case)
    3 / 2 #float division; result is 1 in Python 2 and 1.5 in Python 3
     
    3 // 2 #integer division; result is 1 in Python 2 and Python 3
     
    #Numbers - order of evaluation in math operations
    #Highest priority: raising to a power; Medium priority: division, multiplication and modulo; Low priority: addition and subtraction
    100 - 5 ** 2 / 5 * 2 #1st: 5 ** 2, second: / then *, third - ; result is 90.0
     
    #Numbers - conversion between numeric types
    int(1.5) #result is 1
     
    float(2) #result is 2.0
     
    #Numbers - useful functions
    abs(5) #the distance between the number in between parantheses and 0
     
    abs(-5) #returns the same result as abs(5)
     
    max(1, 2) #returns the largest number
     
    min(1, 2) #returns the smallest number
     
    pow(3, 2) #another way of raising to a power
	
Notebook - Booleans and Logical Operators
Section 4, Lecture 21

    #Booleans - logical operations
    (1 == 1) and (2 == 2) #result is True; AND means that both operands should be True in order to get the expression evaluated as True
     
    (1 == 1) or (2 == 2) #result is True; when using OR, it is enough if only one expression is True, in order to have True as the final result
     
    not(1 == 1) #result is False; using the NOT operator means denying an expression, in this case denying a True expression
     
    not(1 == 2) #result is True; using the NOT operator means denying an expression, in this case denying a False expression
     
    None, 0, 0.0, 0L, 0j, empty string, empty list, empty tuple, empty dictionary #these values always evaluate to False
     
    bool(None) #returns False; function that evaluates values and expressions
     
    bool(0) #returns False; function that evaluates values and expressions
     
    bool(2) #returns True; function that evaluates values and expressions
     
    bool("router") #returns True; function that evaluates values and expressions


#Notebook - Lists
#Section 5, Lecture 26

    #Lists
    list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]  #creating a list
     
    len(list) #returns the number of elements in the list
     
    list1[0] #returns "Cisco" which is the first element in the list (index 0)
     
    list1[0] = "HP" #replacing the first element in the list with another value
     
    #Lists - methods
    list2 = [-11, 2, 12]
     
    min(list2) #returns the smallest element (value) in the list
     
    max(list2) #returns the largest element (value) in the list
     
    list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
     
    list1.append(100) #appending a new element to the list
     
    del list1[4] #removing an element from the list by index
     
    list1.pop(0) #removing an element from the list by index
     
    list1.remove("HP") #removing an element from the list by value
     
    list1.insert(2, "Nortel") #inserting an element at a particular index
     
    list1.extend(list2) #appending a list to another list
     
    list1.index(-11) #returns the index of element -11
     
    list1.count(10) #returns the number of times element 10 is in the list
     
    list2 = [9, 99, 999, 1, 25, 500]
     
    list2.sort() #sorts the list elements in ascending order; modifies the list in place
     
    list2.reverse() #sorts the list elements in descending order; modifies the list in place
     
    sorted(list2) #sorts the elements of a list in ascending order and creates a new list at the same time
     
    sorted(list2, reverse = True) #sorts the elements of a list in descending order and creates a new list at the same time
     
    list1 + list2 #concatenating two lists
     
    list1 * 3 #repetition of a list
     
    #Lists - slicing (works the same as string slicing, but with list elements instead of string characters)
    a_list[5:15] #slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice
    a_list[5:] #slice starting at index 5 up to the end of the list
    a_list[:10] #slice starting at the beginning of the list up to, but NOT including, index 10
    a_list[:] #returns the entire list
    a_list[-1] #returns the last element in the list
    a_list[-2] #returns the second to last element in the list
    a_list[-9:-1] #extracts a certain sublist using negative indexes
    a_list[-5:] #returns the last 5 elements in the list
    a_list[:-5] #returns the list minus its last 5 elements
    a_list[::2] #adds a third element called step; skips every second element of the list
    a_list[::-1] #returns a_list's elements in reverse order
	
Notebook - Sets and Frozensets
Section 6, Lecture 30

    #Sets - unordered collections of unique elements
    set1 = {"1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"} #creating a set
     
    list1 = [11, 12, 13, 14, 15, 15, 15, 11]
    string1 = "aaabcdeeefgg"
     
    set1 = set(list1) #creating a set from a list; removing duplicate elements; returns {11, 12, 13, 14, 15}
     
    set2 = set(string1) #creating a set from a string; removing duplicate characters; returns {'b', 'a', 'g', 'f', 'c', 'd', 'e'}; remeber that sets are UNORDERED collections of elements
     
    len(set1) #returns the number of elements in the set
     
    11 in set1 #returns True; checking if a value is an element of a set
     
    10 not in set 1 #returns True; checking if a value is an element of a set
     
    set1.add(16) #adding an element to a set
     
    set1.remove(16) #removing an element from a set
     
    #Frozensets - immutable sets. The elements of a frozenset remain the same after creation.
    fs1 = frozenset(list1) #defining a frozenset
     
    fs1
    frozenset({11, 12, 13, 14, 15}) #the result
     
    type(fs1)
    <class 'frozenset'> #the result
     
    #proving that frozensets are indeed immutable
    fs1.add(10)
    AttributeError: 'frozenset' object has no attribute 'add'
     
    fs1.remove(1)
    AttributeError: 'frozenset' object has no attribute 'remove'
     
    fs1.pop()
    AttributeError: 'frozenset' object has no attribute 'pop'
     
    fs1.clear()
    AttributeError: 'frozenset' object has no attribute 'clear'
     
    #Sets - methods
    set1.intersection(set2) #returns the common elements of the two sets
     
    set1.difference(set2) #returns the elements that set1 has and set2 doesn't
     
    set1.union(set2) #unifying two sets; the result is also a set, so there are no duplicate elements; not to be confused with concatenation
     
    set1.pop() #removes a random element from the set; set elements cannot be removed by index because sets are UNORDERED collections of elements, so there are no indexes to use
     
    set1.clear() #clearing a set; the result is an empty set

Notebook - Tuples
Section 7, Lecture 33

    #Tuples - immutable lists (their contents cannot be changed by adding, removing or replacing elements)
    my_tuple = () #creating an empty tuple

    my_tuple = (9,) #creating a tuple with a single element; DO NOT forget the comma

    my_tuple = (1, 2, 3, 4)

    #Tuples - the same indexing & slicing rules apply as for strings and lists
    len(my_tuple) #returns the number of elements in the tuple

    my_tuple[0] #returns the first element in the tuple (index 0)
    my_tuple[-1] #returns the last element in the tuple (index -1)
    my_tuple[0:2] #returns (1, 2)
    my_tuple[:2] #returns (1, 2)
    my_tuple[1:] #returns (2, 3, 4)
    my_tuple[:] #returns (1, 2, 3, 4)
    my_tuple[:-2] #returns (1, 2)
    my_tuple[-2:] #returns (3, 4)
    my_tuple[::-1] #returns (4, 3, 2, 1)
    my_tuple[::2] #returns (1, 3)

    #Tuples - tuple assignment / packing and unpacking
    tuple1 = ("Cisco", "2600", "12.4")

    (vendor, model, ios) = tuple1 #vendor will be mapped to "Cisco" and so are the rest of the elements with their corresponding values; both tuples should have the same number of elements

    (a, b, c) = (1, 2, 3) #assigning values in a tuple to variables in another tuple

    min(tuple1) #returns "12.4"

    max(tuple1) #returns "Cisco"

    tuple1 + (5, 6, 7) #tuple concatenation

    tuple1 * 20 #tuple multiplication

    "2600" in tuple1 #returns True

    784 not in tuple1 #returns True

    del tuple1 #deleting a tuple


#Ranges - unlike in Python 2, where the range() function returned a list, in Python 3 it returns an iterator; cannot be sliced
    r = range(10)   #defining a range

    r
    range(0, 10) #the result

    type(r)
    <class 'range'> #the result

    list(r) #converting a range to a list
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  #the result

    list(r)[2:5]    #slicing a range by using the list() function first
    [2, 3, 4]   #the result








