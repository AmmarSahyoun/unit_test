class Phonebook:
    def __init__(self):
        self.numbers = {}
        self.filenme = "phonebook.txt"
        self.cache = open(self.filenme, 'w')


    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def names(self):
        return set(self.numbers.keys())