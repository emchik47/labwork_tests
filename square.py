import unittest


def area(a):
    ''' Принимает сторону квадрата a и возвращает его площадь '''
    if (a <= 0):
        print('Error. Negative number or zero was entered')
        return -1
    
    return a * a


def perimeter(a):
    ''' Принимает сторону квадрата a и возвращает его периметр '''
    if (a <= 0):
        print('Error. Negative number or zero was entered')
        return -1
    
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
       res = area(0)
       self.assertEqual(res, -1)
    
    def test_zero_perimeter(self):
       res = perimeter(0)
       self.assertEqual(res, -1)
    
    def test_correct_perimeter(self):
        res = perimeter(9)
        self.assertEqual(res, 36)
    
    def test_correct_area(self):
        res = area(15)
        self.assertAlmostEqual(res, 225)
    
    def test_negative_area(self):
        res = area(-7)
        self.assertEqual(res, -1)
    
    def test_negative_perimeter(self):
        res = perimeter(-52)
        self.assertEqual(res, -1)