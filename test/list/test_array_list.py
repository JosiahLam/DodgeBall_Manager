import unittest
from list.array_list import ArrayList


class TestArrayList(unittest.TestCase):

    def setUp(self):
        """sets up values before each unit test"""

        # a typical case - numbers
        self._typical1_int = ArrayList()
        self._typical1_int.append(5)
        self._typical1_int.append(9)
        self._typical1_int.append(0)
        self._typical1_int.append(4)
        self._typical1_int.append(5)
        self._typical1_int.append(-2)

        # a typical case - tuples (to test maps)
        self._typical2_tuple = ArrayList()
        self._typical2_tuple.append( ('Latte', 5.49) )
        self._typical2_tuple.append( ('Drip Coffee', 2.19) )
        self._typical2_tuple.append( ('Caramel Frappuccino', 6.79) )

        # an unusual case (empty)
        self._unusual1_empty = ArrayList()

        # an unusual case (one item)
        self._unusual2_oneitem = ArrayList()
        self._unusual2_oneitem.append("oneitem")


    def test_sort_typical_ascending(self):
        # input: 5,9,0,4,5,-2
        # expected output: -2,0,4,5,5,9

        self.assertEqual(6, self._typical1_int.length())  
        self.assertEqual(5, self._typical1_int.get(0))  
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(0, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))
        self._typical1_int.sort()
        self.assertEqual(6, self._typical1_int.length())  
        self.assertEqual(-2, self._typical1_int.get(0))
        self.assertEqual(0, self._typical1_int.get(1))
        self.assertEqual(4, self._typical1_int.get(2))
        self.assertEqual(5, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(9, self._typical1_int.get(5))


    def test_sort_typical_descending(self):
        # input: 5,9,0,4,5,-2
        # expected output: 9,5,5,4,0,-2

        self.assertEqual(6, self._typical1_int.length())  
        self.assertEqual(5, self._typical1_int.get(0))  
        self.assertEqual(9, self._typical1_int.get(1))
        self.assertEqual(0, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(5, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))
        self._typical1_int.sort(descending=True)
        self.assertEqual(6, self._typical1_int.length())  
        self.assertEqual(9, self._typical1_int.get(0))
        self.assertEqual(5, self._typical1_int.get(1))
        self.assertEqual(5, self._typical1_int.get(2))
        self.assertEqual(4, self._typical1_int.get(3))
        self.assertEqual(0, self._typical1_int.get(4))
        self.assertEqual(-2, self._typical1_int.get(5))


    def test_sort_typical_keymap1_ascending(self):
        # input: ('Latte', 5.49), ('Drip Coffee', 2.19), ('Caramel Frappuccino', 6.79)
        # output: ('Caramel Frappuccino', 6.79), ('Drip Coffee', 2.19), ('Latte', 5.49)
        
        self.assertEqual(3, self._typical2_tuple.length())  
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(0))  
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(1))
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2))
        
        # sort by name
        self._typical2_tuple.sort(map_to_key=lambda x : x[0])
        
        self.assertEqual(3, self._typical2_tuple.length())          
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(0))
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(1))
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(2))  


    def test_sort_typical_keymap2_ascending(self):
        # input: ('Latte', 5.49), ('Drip Coffee', 2.19), ('Caramel Frappuccino', 6.79)
        # output: ('Drip Coffee', 2.19), ('Latte', 5.49), ('Caramel Frappuccino', 6.79)

        self.assertEqual(3, self._typical2_tuple.length())         
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(0))  
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(1))
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2))

        # sort by price
        self._typical2_tuple.sort(map_to_key=lambda x : x[1])

        self.assertEqual(3, self._typical2_tuple.length()) 
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(0))
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(1))  
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2))

    def test_sort_typical_keymap1_descending(self):
        # input: ('Latte', 5.49), ('Drip Coffee', 2.19), ('Caramel Frappuccino', 6.79)
        # output: ('Latte', 5.49), ('Drip Coffee', 2.19), ('Caramel Frappuccino', 6.79)

        self.assertEqual(3, self._typical2_tuple.length()) 
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(0))  
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(1))
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2))
        # sort by name
        self._typical2_tuple.sort(map_to_key=lambda x : x[0], descending=True)

        self.assertEqual(3, self._typical2_tuple.length()) 
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(0))  
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(1))
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2))


    def test_sort_typical_keymap2_descending(self):
        # input: ('Latte', 5.49), ('Drip Coffee', 2.19), ('Caramel Frappuccino', 6.79)
        # output: ('Caramel Frappuccino', 6.79), ('Latte', 5.49), ('Drip Coffee', 2.19)
        
        self.assertEqual(3, self._typical2_tuple.length()) 
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(0))  
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(1))
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(2))

        # sort by price
        self._typical2_tuple.sort(map_to_key=lambda x : x[1], descending=True)

        self.assertEqual(3, self._typical2_tuple.length()) 
        self.assertEqual(('Caramel Frappuccino', 6.79), self._typical2_tuple.get(0))
        self.assertEqual(('Latte', 5.49), self._typical2_tuple.get(1))  
        self.assertEqual(('Drip Coffee', 2.19), self._typical2_tuple.get(2))


    def test_sort_unusual1_empty(self):
        # input: <empty>
        # output: <empty> (no changes)
        self.assertEqual(0, self._unusual1_empty.length())
        self._unusual1_empty.sort()
        self.assertEqual(0, self._unusual1_empty.length())
        self._unusual1_empty.sort(descending=True)
        self.assertEqual(0, self._unusual1_empty.length())


    def test_sort_unusual2_onetime(self):
        # input: "oneitem"
        # output: "oneitem" (no changes)
        
        self.assertEqual(1, self._unusual2_oneitem.length())
        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))

        # sort
        self._unusual2_oneitem.sort()

        self.assertEqual(1, self._unusual2_oneitem.length())
        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))

        # sort descending
        self._unusual2_oneitem.sort(descending=True)

        self.assertEqual("oneitem", self._unusual2_oneitem.get(0))
        self.assertEqual(1, self._unusual2_oneitem.length())




    