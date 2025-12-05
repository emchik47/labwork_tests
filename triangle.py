import unittest


def area(a, h):
    if (a <= 0 or h <= 0):
        print('Error. Negative number or zero was entered')
        return -1
    
    return a * h / 2 

def perimeter(a, b, c):
    if (a <= 0 or b <= 0 or c <= 0):
        print('Error. Negative number or zero was entered')
        return -1
    
    if (a + b <= c or a + c <= b or b + c <= a):
        print('Error. Wrong sides length')
        return -1
    
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
       res = area(0, 10)
       self.assertEqual(res, -1)
       res = area(7, 0)
       self.assertEqual(res, -1)
    
    def test_zero_perimeter(self):
       res = perimeter(0, 1, 2)
       self.assertEqual(res, -1)
       res = perimeter(1, 0, 2)
       self.assertEqual(res, -1)
       res = perimeter(2, 1, 0)
       self.assertEqual(res, -1)
       res = perimeter(0, 0, 0)
       self.assertEqual(res, -1)
    
    def test_correct_perimeter(self):
        res = perimeter(10, 20, 11)
        self.assertEqual(res, 41)
    
    def test_correct_area(self):
        res = area(5, 6)
        self.assertEqual(res, 15)
    
    def test_negative_area(self):
        res = area(-1, 100)
        self.assertEqual(res, -1)
    
    def test_wrong_sides_length(self):
        res = perimeter(10, 20, 30)
        self.assertEqual(res, -1)
    
    def test_negative_perimeter(self):
        res = perimeter(-10, 50, 50)
        self.assertEqual(res, -1)