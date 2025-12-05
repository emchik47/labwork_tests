import unittest


def area(a, b):
    if (a <= 0 or b <= 0):
        print('Error. Negative number or zero was entered')
        return -1
    
    return a * b 

def perimeter(a, b):
    if (a <= 0 or b <= 0):
        print('Error. Negative number or zero was entered')
        return -1
    
    return 2 * (a + b)

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, -1)
       
    def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)
    
    def test_correct_perimeter(self):
        res = perimeter(10, 20)
        self.assertEqual(res, 60)
    
    def test_correct_area(self):
        res = area(5, 6)
        self.assertEqual(res, 30)
    
    def test_negative_area(self):
        res = area(-1, 100)
        self.assertEqual(res, -1)
    
    def test_negative_perimeter(self):
        res = perimeter(-10, 50)
        self.assertEqual(res, -1)
    
