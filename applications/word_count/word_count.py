from hashtable import HashTable
import re

hash_table = HashTable()
def word_count(s):
    # Your code here
    word_cache = {}

    if s:
        sentence = s.split(" ")
        for word_arr in sentence:
            # replace every char not a-z, apostrophe, or A-Z with spaces, then remove all spaces
            word_arr = re.sub("[^a-z'A-Z]", " ", word_arr).split(" ")
            for word in word_arr:
                word = word.lower() # make every word lowercase
                if word in word_cache:   # check if word is in word_cache
                    word_cache[word] += 1   # if so, increment the value of it's index by 1
                else:
                    word_cache[word] = 1   # if not, set it to 1
                      
        if "" in word_cache:
            del word_cache[""] 

    print(f'WORD CACHE: {word_cache}')
    return word_cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))