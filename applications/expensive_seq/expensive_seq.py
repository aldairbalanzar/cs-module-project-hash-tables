# Your code here
from hashtable import HashTable

hash_table = HashTable()
def expensive_seq(x, y, z):
    # Your code here
    index = str(x) + str(y) + str(z)

    if x <= 0:
        total = y + z
        hash_table.put(index, total)
        return hash_table.get(index)
    elif hash_table.get(index):
        return hash_table.get(index)
    else:
        total = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z * 2) + expensive_seq(x-3, y+3, z*3)
        hash_table.put(index, total)
        return hash_table.get(index)

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
