import math
import unittest

def area(r):
    ''' Принимает радиус r круга и возвращает его площадь '''
    if (r <= 0):
        print('Error. Negative number or zero was entered')
        return -1
    
    return math.pi * r * r


def perimeter(r):
    ''' Принимает радиус r круга и возвращает его периметр '''
    if (r <= 0):
        print('Error. Negative number or zero was entered')
        return -1
    
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
       res = area(0)
       self.assertEqual(res, -1)
    
    def test_zero_perimeter(self):
       res = perimeter(0)
       self.assertEqual(res, -1)
    
    def test_correct_perimeter(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 62.83, places=2)
    
    def test_correct_area(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.54, places=2)
    
    def test_negative_area(self):
        res = area(-6)
        self.assertEqual(res, -1)
    
    def test_negative_perimeter(self):
        res = perimeter(-10)
        self.assertEqual(res, -1)