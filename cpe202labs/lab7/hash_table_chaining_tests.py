# Justin Mo
import unittest
from hash_table_chaining import *
class TestHash(unittest.TestCase):
    def test_empty_repr(self):
        hash1 = empty_hash_table()
        self.assertEqual(repr(hash1), "Size: 8, List: [None, None, None, None, None, None, None, None]")
        val = Value(5, 5)
        self.assertEqual(repr(val), "(Key: 5, Val: 5)")

    def test_get(self):
        hash1 = empty_hash_table()
        hash1.list_of_vals = [[Value(0, 0)], [Value(1, 1)], None, None, None, None, None, [Value(7, 7)]]
        self.assertEqual(get(hash1, 1), 1)
        self.assertEqual(get(hash1, 7), 7)
        with self.assertRaises(LookupError):
            get(hash1, 2)
        with self.assertRaises(LookupError):
            get(hash1, 8)
        
    def test_remove(self):
        hash1 = empty_hash_table()
        hash1.list_of_vals = [[Value(8, 0)], [Value(1, 1)], None, None, None, None, None, [Value(7, 7)]]
        hash2 = empty_hash_table()
        hash2.list_of_vals = [None, [Value(1, 1)], None, None, None, None, None, [Value(7, 7)]]
        self.assertEqual(remove(hash1, 8), hash2)
        hash3 = empty_hash_table()
        hash3.list_of_vals = [[Value(0, 0), Value(8, 0), Value(16, 0)], None, None, None, None, None, None, None]
        hash4 = empty_hash_table()
        hash4.list_of_vals = [[Value(0, 0), Value(16, 0)], None, None, None, None, None, None, None]
        self.assertEqual(remove(hash3, 8), hash4)
        hash5 = empty_hash_table()
        hash5.list_of_vals = [[Value(0, 0), Value(8, 0), Value(16, 0)], None, None, None, None, None, None, None]
        hash6 = empty_hash_table()
        hash6.list_of_vals = [[Value(8, 0), Value(16, 0)], None, None, None, None, None, None, None] 
        self.assertEqual(remove(hash5, 0), hash6)
        with self.assertRaises(LookupError):
            remove(hash6, 1)
        with self.assertRaises(LookupError):
            remove(hash6, 0)

    def test_size(self):
        hash1 = empty_hash_table()
        hash1.list_of_vals = [[Value(0, 0), Value(8, 0), Value(16, 0)], None, None, None, None, None, None, [Value(7, 0)]] 
        self.assertEqual(size(hash1), 4)

    def test_load_factor(self):
        hash1 = empty_hash_table()
        hash1.list_of_vals = [[Value(0, 0), Value(8, 0), Value(16, 0)], None, None, None, None, None, None, [Value(7, 0)]]
        self.assertEqual(load_factor(hash1), 0.5)

    def test_collisions(self):
        hash1 = empty_hash_table()
        hash1.list_of_vals = [[Value(0, 0), Value(8, 0), Value(16, 0)], None, None, None, None, None, None, [Value(7, 0)]]
        self.assertEqual(collisions(hash1), 2)
        hash2 = empty_hash_table()
        hash2.list_of_vals = [[Value(8, 0), Value(16, 0)], None, None, None, None, None, None, None]
        self.assertEqual(collisions(hash2), 1)
        hash3 = empty_hash_table()
        hash3.list_of_vals = [[Value(8, 0), Value(16, 0)], None, None, [Value(11, 0), Value(19, 0)], None, None, None, None]
        self.assertEqual(collisions(hash3), 2)

if __name__ == "__main__":
    unittest.main()
