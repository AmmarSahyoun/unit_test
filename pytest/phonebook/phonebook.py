import os

class Phonebook:
    def __init__(self, cache_directory):
        self.numbers = {}
        #pytest has feature to use a temporary directory
        self.filename = os.path.join(cache_directory, "phonebook.txt")
        self.cache = open(self.filename, 'w') # open cache file from the


    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def names(self):
        return set(self.numbers.keys())

    def clear(self):
        self.cache.close()
        os.remove(self.filename) # removed it from the filesystem