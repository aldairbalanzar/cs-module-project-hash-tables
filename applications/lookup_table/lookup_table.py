# Your code here
import math
import random

# import hash table logic from yesterday because
# it already handles collision and growth
from hashtable import HashTable, HashTableEntry

def slowfun_too_slow(x, y):
    v = math.pow(x, y)      # math.pow() - returns value of 1st argument raised to the power of 2nd argument
    v = math.factorial(v)   # math.factorial() - returns factorial product of number entered
    v //= (x + y)           # divide and floor by the sum of x and y
    v %= 982451653          # finds remainder of v divided by 982451653

    return v    # you're returning v's value after messing it up in this function

# make a hash table to store the key and value of v from the function above
hash_table = HashTable()

def slowfun(x, y):
    # Your code here
    # key should be a string of the numbers passed in
    index = str(x) + str(y)
    # check if value exists in hash table (we already have get logic)
    if hash_table.get(index):
        return hash_table.get(index)
    # if not, run it through the logic from function above
    # then use put() method to add it to the the hash table using
    # index and variable storing the value after running it through logic
    else:
        v = math.pow(x, y)     
        v = math.factorial(v)   
        v //= (x + y)           
        v %= 982451653       
        hash_table.put(index, v)
        return v

    

    

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14) # randrange() - returns random integer from specified range (start, stop, step)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
