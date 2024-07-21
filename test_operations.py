import unittest
from operations import Operations

class TestOperations(unittest.TestCase):
    
    def setUp(self) -> None:
        self.ops = Operations()
    
    def test_add(self):
        self.assertEqual(self.ops.plus([1,2]), 3)
        self.assertEqual(self.ops.plus([0,0]), 0)
        self.assertEqual(self.ops.plus([-1,3]), 2)
    
    def test_subtraction(self): 
        self.assertEqual(self.ops.minus([1,1]), 0)    
        self.assertEqual(self.ops.minus([-7,-8]), 1)    
    
    def test_multiplcation(self):
        self.assertEqual(self.ops.multiplication([0,0]), 0)
        self.assertEqual(self.ops.multiplication([0,1]), 0)
        self.assertEqual(self.ops.multiplication([5,11]), 55)
   
    def test_division(self):
        self.assertEqual(self.ops.division([1,1]), 1)  
        self.assertEqual(self.ops.division([2,4]), .5)  
        self.assertEqual(self.ops.division([4,2]), 2)  

if  __name__ == '__main__': 
    unittest.main()