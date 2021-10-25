import pytest
from phonebook import Phonebook


@pytest.fixture # to send it as argument, instead of use setUp in unittest
def phonebook(tmpdir):
    "Provide an empty Phonebook"
    return Phonebook(tmpdir)
#(tmpdir)Return a temporary directory path object which is unique to each test
#function invocation, created as a sub directory of the base temporary directory.

def test_lookup_by_name(phonebook):
    phonebook.add('Bob', '1234')
    assert '1234' == phonebook.lookup('Bob')

def test_phonebook_contains_all_names(phonebook):
    phonebook.add('Bob', '1234')
    assert  'Bob' in phonebook.names()

def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup('Bob')



# pytest --fixtures