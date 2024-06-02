import unittest
from TreeSet import TreeSet

class TestTreeSet(unittest.TestCase):
    def test_add_elements(self):
        """Test to verify that elements can be added to the set correctly and duplicate verification."""
        ts = TreeSet()
        self.assertTrue(ts.add(5))
        self.assertTrue(ts.add(10))
        self.assertTrue(ts.add(3))
        self.assertEqual(ts.size(), 3)
        self.assertTrue(ts.add(1))
        self.assertFalse(ts.add(5))

    def test_add_different_types(self):
        """Test to verify that different types cannot be mixed in the set."""
        ts = TreeSet()
        ts.add(10)
        with self.assertRaises(TypeError):
            ts.add("test")

    def test_contains(self):
        """Test to verify if the set contains certain elements."""
        ts = TreeSet()
        ts.add(1)
        ts.add(2)
        ts.add(3)
        self.assertTrue(ts.contains(1))
        self.assertFalse(ts.contains(4))

    def test_remove(self):
        """Test to verify element removal and that an absent element cannot be removed."""
        ts = TreeSet()
        ts.add(1)
        ts.add(2)
        ts.add(3)
        self.assertTrue(ts.remove(2))
        self.assertFalse(ts.contains(2))
        self.assertEqual(ts.size(), 2)
        self.assertFalse(ts.remove(2))

    def test_first_last_elements(self):
        """Test to verify that the first and last elements of the set can be obtained."""
        ts = TreeSet()
        ts.add(3)
        ts.add(1)
        ts.add(5)
        self.assertEqual(ts.first(), 1)
        self.assertEqual(ts.last(), 5)

    def test_clear_and_empty(self):
        """Test to verify that the set can be cleared and checked if it is empty."""
        ts = TreeSet()
        ts.add(1)
        ts.add(2)
        ts.clear()
        self.assertTrue(ts.isEmpty())

    def test_poll_methods(self):
        """Test to verify the functionality of pollFirst and pollLast."""
        ts = TreeSet()
        ts.add(1)
        ts.add(2)
        ts.add(3)
        self.assertEqual(ts.pollFirst(), 1)
        self.assertEqual(ts.pollLast(), 3)
        self.assertEqual(ts.size(), 1)

    def test_iterators(self):
        """Test to verify that iterators iterate correctly in normal and descending order."""
        ts = TreeSet()
        elements = [3, 1, 4, 2]
        for e in elements:
            ts.add(e)
        sorted_elements = sorted(elements)
        self.assertEqual(list(ts.iterator()), sorted_elements)
        self.assertEqual(list(ts.descendingIterator()), sorted_elements[::-1])

    def test_ceiling_floor(self):
        """Test to verify the ceiling and floor operations in the set."""
        ts = TreeSet()
        ts.add(5)
        ts.add(10)
        ts.add(15)
        ts.add(20)
        self.assertEqual(ts.ceiling(12), 15)
        self.assertEqual(ts.floor(12), 10)

    def test_higher_lower(self):
        """Test to verify the higher and lower operations in the set."""
        ts = TreeSet()
        ts.add(3)
        ts.add(6)
        ts.add(9)
        self.assertEqual(ts.higher(4), 6)
        self.assertEqual(ts.lower(8), 6)

    def test_type_error_on_empty_remove(self):
        """Test to verify that an attempt to remove from an empty set is handled correctly."""
        ts = TreeSet()
        self.assertFalse(ts.remove(5))

    def test_type_consistency_after_clear(self):
        """Test to verify that data type consistency is maintained even after clearing the set."""
        ts = TreeSet()
        ts.add(10)
        ts.clear()
        # This should not raise an error because the set was cleared
        ts.add("test")

    def test_empty_set_operations(self):
        """Test to verify operations on an empty set."""
        ts = TreeSet()
        self.assertTrue(ts.isEmpty())
        self.assertEqual(ts.size(), 0)
        self.assertIsNone(ts.first())
        self.assertIsNone(ts.last())
        self.assertIsNone(ts.pollFirst())
        self.assertIsNone(ts.pollLast())

    def test_duplicates_handling(self):
        """Test to verify that duplicates are not added to the set."""
        ts = TreeSet()
        ts.add(1)
        ts.add(1)
        self.assertEqual(ts.size(), 1)
        ts.add(2)
        ts.add(2)
        self.assertEqual(ts.size(), 2)

    def test_boundaries_of_ceiling_floor(self):
        """Test to verify ceiling and floor at boundaries."""
        ts = TreeSet()
        ts.add(10)
        ts.add(20)
        self.assertEqual(ts.ceiling(10), 10)
        self.assertEqual(ts.floor(20), 20)
        self.assertEqual(ts.ceiling(5), 10)
        self.assertEqual(ts.floor(25), 20)

    def test_boundaries_of_higher_lower(self):
        """Test to verify higher and lower at boundaries."""
        ts = TreeSet()
        ts.add(10)
        ts.add(20)
        self.assertEqual(ts.higher(10), 20)
        self.assertIsNone(ts.higher(20))
        self.assertEqual(ts.lower(20), 10)
        self.assertIsNone(ts.lower(10))

    def test_mixed_type_handling(self):
        """Test to verify that set does not accept mixed types after initial type is set."""
        ts = TreeSet()
        ts.add(1)
        with self.assertRaises(TypeError):
            ts.add("string")
        ts.clear()
        ts.add("string")
        with self.assertRaises(TypeError):
            ts.add(1)

    def test_large_number_of_elements(self):
        """Test the performance and correctness with a large number of elements."""
        ts = TreeSet()
        num_elements = 1000
        for i in range(num_elements):
            ts.add(i)
        self.assertEqual(ts.size(), num_elements)
        self.assertEqual(ts.first(), 0)
        self.assertEqual(ts.last(), num_elements - 1)
        for i in range(num_elements):
            self.assertTrue(ts.contains(i))
        for i in range(num_elements):
            self.assertTrue(ts.remove(i))
        self.assertTrue(ts.isEmpty(), f"Set is not empty after removing all elements: {ts.size()} remaining")

if __name__ == '__main__':
    unittest.main()
