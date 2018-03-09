import unittest
from verySimpleMath import VerySimpleMath



class TestVerySimpleMath(unittest.TestCase):
  
    def setUp(self):
      self.obj = VerySimpleMath()
      
    def test_initialState(self):
      self.assertEqual(self.obj.state,0)
      
    def test_summation(self):
      self.obj.increment_state()
      self.assertEqual(self.obj.state, 1)
      
    def test_subtraction(self):
      self.obj.decrement_state()
      self.assertEqual(self.obj.state, -1)
      
    def test_clear(self):
      self.obj.clear_state()
      self.assertEqual(self.obj.state, 0)

if __name__ == '__main__':
  unittest.main()