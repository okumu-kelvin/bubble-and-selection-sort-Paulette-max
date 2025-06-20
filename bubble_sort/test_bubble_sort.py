import unittest
from bubble_sort import bubble_sort

class testBubbleSort(unittest.TestCase):
    def test_sorted(self):
     self.assertEqual(bubble_sort([1, 2, 3]) == [1, 2, 3])

    def test_reverse(self):
        self.assertEqual(bubble_sort([3, 2, 1]) == [1, 2, 3])

    def test_duplicates(self):
        self.assertEqual(bubble_sort([4, 5, 3, 4]) == [3, 4, 4, 5])
