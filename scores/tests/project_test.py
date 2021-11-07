import unittest
import bubblesort as st
import file_max_cell as fs

class Project_test(unittest.TestCase):
    def test_bsort(self):
        testlist = [4,3,2,1]
        expected = [1,2,3,4]
        actual = st.bubblesort(testlist)
        self.assertEqual(actual, expected)

    def test_desc(self):
        testlist = [1,2,5,4,3]
        expected = [5,4,3,2,1]
        actual = st.bubblesort(testlist, 1)
        self.assertEqual(actual, expected)

    def test_empty(self):
        testlist = []
        expected = []
        actual = st.bubblesort(testlist)
        self.assertEqual(actual, expected)

    def test_file_max_cell(self):
        a_max, a_series = fs.file_max_cell('../scores.csv', 'math score')
        self.assertEqual(a_max, 100)
        self.assertEqual(len(a_series), 8)