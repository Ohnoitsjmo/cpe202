# Justin Mo
import unittest
from hash_table_chaining import *

class TestHash(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(repr(Pair(3, "mt")), str(Pair(3, "mt")))
    
    def test_length(self):
        self.assertEqual(length(Pair(4, Pair(3, None))), 2)
        self.assertEqual(length(None), 0)

    def test_add(self):
        self.assertEqual(addd(Pair(1, Pair(3, None)), 1, 2), Pair(1, Pair(2, Pair(3, None))))
        self.assertEqual(addd(Pair(3, None), 0, 9), Pair(9, Pair(3, None)))
        with self.assertRaises(IndexError):
            addd(Pair(3, None), 5, 9)
        self.assertEqual(addd(Pair(3, None), 1, 9), Pair(3, Pair(9, None)))
        self.assertEqual(addd(None, 0, 5), Pair(5, None))

    def test_set(self):
        with self.assertRaises(IndexError):
            sett(None, 4, 5), Pair(5, None)
        self.assertEqual(sett(Pair(2, None), 0, 5), Pair(5, None))
        self.assertEqual(sett(Pair(2, Pair(3, Pair(5, None))), 1, 5), Pair(2, Pair(5, Pair(5, None))))
        self.assertEqual(sett(Pair(2, Pair(3, None)), 1, 5), Pair(2, Pair(5, None)))

    def test_remove_helper(self):
        self.assertEqual(remove_helper(Pair(1, Pair(2, None)), 0), 1)
        with self.assertRaises(IndexError):
            remove_helper(None, 2)
        with self.assertRaises(IndexError):
            remove_helper(Pair(1, Pair(2, None)), 3)
    
    def test_remove_helper2(self):
        with self.assertRaises(IndexError):
            remove_helper2(None, 2)
        with self.assertRaises(IndexError):
            remove_helper2(Pair(1, Pair(2, None)), 3)
    
    def test_empty_repr(self):
        hash1 = empty_hash_table()    
        self.assertEqual(repr(hash1), "Capacity: 8, Size: 0, Collisions: 0, List: [None, None, None, None, None, None, None, None]")
        val = Item(5, 5)
        self.assertEqual(repr(val), "(Key: 5, Val: 5)")

    def test_insert(self):
        hash1 = empty_hash_table()
        hash2 = empty_hash_table()
        hash2.list_of_vals = [Pair(Item(0, 0), None), None, None, None, None, None, None, None]
        hash2.size = 1
        self.assertEqual(insert(hash1, 0, 0), hash2)
        hash3 = empty_hash_table()
        hash3.size = 2
        hash3.collisions = 1
        hash3.list_of_vals = [Pair(Item(0, 0), Pair(Item(8, 8), None)), None, None, None, None, None, None, None]
        hash4 = empty_hash_table()
        hash4.size = 3
        hash4.collisions = 2
        hash4.list_of_vals = [Pair(Item(16, 16), Pair(Item(0, 0), Pair(Item(8, 8), None))), None, None, None, None, None, None, None]
        #print(insert(hash3, 16, 16))
        #print(hash4)
        self.assertEqual(insert(hash3, 16, 16), hash4)
        hash5 = empty_hash_table()
        hash5.collisions = 11
        hash5. size = 12
        hash5.list_of_vals = [Pair(Item(0, 0), Pair(Item(8, 8), Pair(Item(16, 16), Pair(Item(24, 24), Pair(Item(32, 32), Pair(Item(40, 40), Pair(Item(48, 48), Pair(Item(56, 56), Pair(Item(64, 64), Pair(Item(72, 72), Pair(Item(80, 80), Pair(Item(88, 88), None)))))))))))), None, None, None, None, None, None, None]
        insert(hash5, 96, 96)
        hash6 = empty_hash_table()
        hash6.list_of_vals = [Pair(Item(0, 0), None), None, None, None, None, None, None, None] 
        hash7 = hash6
        self.assertEqual(insert(hash6, 0, 0), hash7)
        hash8 = empty_hash_table()
        hash8.size = 13
        hash8.collisions = 12
        hash8.list_of_vals = [Pair(Item(0, 0), Pair(Item(8, 8), Pair(Item(16, 16), Pair(Item(24, 24), Pair(Item(32, 32), Pair(Item(40, 40), Pair(Item(48, 48), Pair(Item(56, 56), Pair(Item(64, 64), Pair(Item(72, 72), Pair(Item(80, 80), Pair(Item(88, 88), Pair(Item(104, 104), None))))))))))))), None, None, None, None, None, None, None]
        insert(hash8, 96, 96)
        insert(hash8, 97, 97)

    def test_get(self):
        hash1 = empty_hash_table()
        hash1.size = 4
        hash1.list_of_vals = [Pair(Item(0, 0), Pair(Item(8, 8), None)), Pair(Item(1, 1), None), None, None, None, None, None, Pair(Item(7, 7), None)]
        self.assertEqual(get(hash1, 1), 1)
        self.assertEqual(get(hash1, 7), 7)
        with self.assertRaises(LookupError):
            get(hash1, 2)
        with self.assertRaises(LookupError):
            get(hash1, 16)

    def test_remove(self):
        hash1 = empty_hash_table()
        hash1.list_of_vals = [Pair(Item(8, 8), None), Pair(Item(1, 1), None), None, None, None, None, None, None, Pair(Item(7, 7), None)]
        hash1.size = 3
        hash2 = empty_hash_table()
        hash2.size = 2
        hash2.list_of_vals = [None, Pair(Item(1, 1), None), None, None, None, None, None, None, Pair(Item(7, 7), None)]
        self.assertEqual(remove(hash1, 8), hash2)
        hash3 = empty_hash_table()
        hash3.size = 3
        hash3.list_of_vals = [Pair(Item(0, 0), Pair(Item(8, 8), Pair(Item(16, 16), None))), None, None, None, None, None, None, None, None] 
        hash4 = empty_hash_table()
        hash4.size = 2
        hash4.list_of_vals = [Pair(Item(0, 0), Pair(Item(16, 16), None)), None, None, None, None, None, None, None, None]
        hash6 = empty_hash_table()
        hash6.size = 2
        hash6.list_of_vals = [Pair(Item(8, 8), Pair(Item(16, 16), None)), None, None, None, None, None, None, None]
        with self.assertRaises(LookupError):
            remove(hash6, 1)
        with self.assertRaises(LookupError):
            remove(hash6, 0)

    def test_size(self):
        hash1 = empty_hash_table()
        hash1.size = 5
        self.assertEqual(size(hash1), 5)
    
    def test_load_factor(self):
        hash1 = empty_hash_table()
        hash1.list_of_vals = [Pair(Item(0, 0), Pair(Item(8, 8), Pair(Item(16, 16), None))), None, None, None, None, None, None, Pair(Item(7, 0), None)]
        hash1.size = 4
        hash1.capacity = 8
        self.assertEqual(load_factor(hash1), 0.5)

    def test_collisions(self):
        hash1 = empty_hash_table()
        hash1.list_of_vals = [Pair(Item(0, 0), Pair(Item(8, 8), Pair(Item(16, 16), None))), None, None, None, None, None, None, Pair(Item(7, 0), None)]
        hash1.size = 4  
        hash1.collisions = 2
        self.assertEqual(collisions(hash1), 2)



if __name__ == "__main__":
    unittest.main()
