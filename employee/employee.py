class Employee:
    raise_amt = 1.05
    def __init__(self, first, last, pay):
        self._first = first
        self._last = last
        self._pay = pay
        self._raise_amt = 1.05

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, new_first):
        self._first = new_first

    @property
    def email(self):
        return "{}.{}@email.com".format(self._first, self._last)

    @property
    def fullnane(self):
        return "{} {}".format(self._first, self._last)

    def apply_raise(self):
        self._pay = int(self._pay * self.raise_amt)
        return self._pay


