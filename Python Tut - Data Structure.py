https://docs.python.org/2/tutorial/datastructures.html

Python Tutorial- Data Structure 
# Basic Types
int
double
float
string

# Dict, List, Tuple
Dict_Example = {"one": 1, "Two": 2} 
List_Example = [1,2,3,4,5] 
Tunple_Example = (1,2,3,4) # immutable, deepcopy

# null object initialization
var1 = None

# floating point arithmetics limitation
round(2.675, 2) gives 2.67

# Exception

raise Exception("msg")


# lambda operator: map(), filter(), reduce()

>>> foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
>>> 
>>> print filter(lambda x: x % 3 == 0, foo)
[18, 9, 24, 12, 27]
>>> 
>>> print map(lambda x: x * 2 + 10, foo)
[14, 46, 28, 54, 44, 58, 26, 34, 64]
>>> 
>>> print reduce(lambda x, y: x + y, foo)
139