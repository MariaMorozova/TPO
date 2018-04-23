# coding=utf-8
'''
	1. Напишите модульные тесты для функций calculateSquare(), calculateAngle(), isTriangle(), getType().
	2. В некоторых из этих функций есть ошибки, поэтому правильно написанные тесты должны падать (обнаруживать эти ошибки)
	3. Исправьте ошибки. Теперь тесты должны проходить (у всех тестов статус ОК).
	4. В указанных функциях есть места, написанные не очень эффективно. Перепишите их. 
	   Удостоверьтесь, что ничего не сломано — все ваши тесты проходят.
	5. Посчитайте покрытие тестами. Для этого используйте инструмент coverage https://pypi.python.org/pypi/coverage
'''

import unittest
import math


class Triangle:
    '''
        a, b, c — стороны треугольника
        класс позволяет определить, является ли это треугольником
        какого типа этот треугольник
        посчитать периметр и площадь
    '''

    def __init__(self, a, b, c):
        self.triangle = [a, b, c]

    def getA(self):
        return self.triangle[0]

    def getB(self):
        return self.triangle[1]

    def getC(self):
        return self.triangle[2]

    def calculatePerimeter(self):
        '''
            расчет периметра
        '''
        return sum(self.triangle)

    def calculateSquare(self):
        '''
            расчет площади по формуле Герона
        '''
        if not (self.isTriangle()):
            return "not triangle"
        a = self.triangle[0]
        b = self.triangle[1]
        c = self.triangle[2]

        p = (a + b + c) / 2.0
        result = (p * (p - a) * (p - b) * (p - c))
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return S

    def calculateAngle(self, angle):
        '''
            Расчет угла по теореме косинусов.
            В качестве параметров передается alpha, beta, gamma — название угла, который нужно посчитать.
            Угол находится напротив соответствующей стороны (a, b, c)
            Возвращает величину угла в градусах
        '''
        a = self.triangle[0]
        b = self.triangle[1]
        c = self.triangle[2]

        adj1 = 1
        adj2 = 1
        adj3 = 1

        if (angle == 'alpha'):
            adj1 = b
            adj2 = c
            opp = a
        elif (angle == 'beta'):
            adj1 = a
            adj2 = c
            opp = b
        elif (angle == 'gamma'):
            adj1 = a
            adj2 = b
            opp = c
        else:
            return False
        if not (self.isTriangle()):
            return "not triangle"
        f = (adj1 ** 2 + adj2 ** 2 - opp ** 2) / (2.0 * adj1 * adj2)
        return math.degrees(math.acos(f))

    def isTriangle(self):
        '''
            Проверка, что треугольник с введенными сторонами вообще может существовать
        '''
        a = self.triangle[0]
        b = self.triangle[1]
        c = self.triangle[2]
        if ((a + b <= c) or (a + c <= b) or (b + c <= a) or (a <= 0) or (b <= 0) or (c <= 0)):
            return False
        else:
            return True

    def getType(self):
        '''
            Возвращает тип треугольника:
            common — просто треугольник
            isosceles — равнобедренный
            equilateral — равносторонний
            right — прямоугольный
        '''
        type = 'common'
        a = self.triangle[0]
        b = self.triangle[1]
        c = self.triangle[2]
        if not (self.isTriangle()):
            return "not triangle"
        if ((a == b) and (a == c) and (b == c)):
            type = 'equilateral'
        elif (((a == b) and (a != c)) or ((a == c) and (a != b)) or ((b == c) and (b != a))):
            type = 'isosceles'
        if ((a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2) or (c ** 2 == a ** 2 + b ** 2)):
            type = 'right'
        return type


class TriangleTest(unittest.TestCase):
    def setUp(self):
        print
        "Test started"

    def tearDown(self):
        print
        "Test finished"

    def testGetA(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.getA(), 3.0)

    def testGetB(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.getB(), 4.0)

    def testGetC(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.getC(), 5.0)

    def testCalculatePerimeter(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.calculatePerimeter(), 12.0)
        t = Triangle(3, 3, 3)
        self.assertAlmostEqual(t.calculatePerimeter(), 9.0)
        t = Triangle(1.2, 1.3, 1.4)
        self.assertAlmostEqual(t.calculatePerimeter(), 3.9)

    def testCalculateSquare(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.calculateSquare(), 6.0)
        t = Triangle(3, 3, 3)
        self.assertAlmostEqual(t.calculateSquare(), 3.897114317029974)

    def testIncorrectParametersCalculateSquare(self):
        t = Triangle(-3, -4, -5)
        self.assertEqual("not triangle", t.calculateSquare())
        t = Triangle(2, 2, 5)
        self.assertEqual("not triangle", t.calculateSquare())
        t = Triangle(0, 0, 0)
        self.assertEqual("not triangle", t.calculateSquare())

    def testCalculateAngle(self):
        t = Triangle(2, 3, 4)
        self.assertAlmostEqual(t.calculateAngle("alpha"), 28.955024372)
        self.assertAlmostEqual(t.calculateAngle("beta"), 46.567463442)
        self.assertAlmostEqual(t.calculateAngle("gamma"), 104.477512186)
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.calculateAngle("alpha"), 36.869897646)
        self.assertAlmostEqual(t.calculateAngle("beta"), 53.130102354)
        self.assertAlmostEqual(t.calculateAngle("gamma"), 90)
        t = Triangle(2, 2, 3)
        self.assertAlmostEqual(t.calculateAngle("alpha"), 41.409622109)
        self.assertAlmostEqual(t.calculateAngle("beta"), 41.409622109)
        self.assertAlmostEqual(t.calculateAngle("gamma"), 97.180755781)
        t = Triangle(3, 3, 3)
        self.assertAlmostEqual(t.calculateAngle("alpha"), 60)
        self.assertAlmostEqual(t.calculateAngle("beta"), 60)
        self.assertAlmostEqual(t.calculateAngle("gamma"), 60)

    def testIncorrectParametersCalculateAngle(self):
        t = Triangle(1, 1, 2)
        self.assertAlmostEqual(t.calculateAngle("alphabtagsdb"), 0)
        t = Triangle(0, 0, 0)
        self.assertEqual("not triangle", t.calculateAngle("alpha"))
        t = Triangle(1, 1, 2)
        self.assertEqual("not triangle", t.calculateAngle("alpha"))

    def testIsTriangle(self):
        t = Triangle(2, 3, 4)  # a + b > c
        self.assertTrue(t.isTriangle())
        t = Triangle(3, 4, 5)  # a + c > b
        self.assertTrue(t.isTriangle())
        t = Triangle(2, 2, 3)  # b + c > a
        self.assertTrue(t.isTriangle())
        t = Triangle(1, 1, 1)  # a = b = c
        self.assertTrue(t.isTriangle())

    def testIsNotTriangle(self):
        t = Triangle(2, 3, 6)  # a + b <= c
        self.assertFalse(t.isTriangle())
        t = Triangle(1, 10, 3)  # a + c <= b
        self.assertFalse(t.isTriangle())
        t = Triangle(12, 3, 5)  # b + c <= a
        self.assertFalse(t.isTriangle())
        t = Triangle(2, 3, 5)  # a + b = c
        self.assertFalse(t.isTriangle())
        t = Triangle(1, 4, 3)  # a + c = b
        self.assertFalse(t.isTriangle())
        t = Triangle(8, 3, 5)  # b + c = a
        self.assertFalse(t.isTriangle())
        t = Triangle(0, -5, 5)
        self.assertFalse(t.isTriangle())

    def testGetType(self):
        t = Triangle(2, 3, 4)
        self.assertEqual("common", t.getType())
        t = Triangle(4, 5, 6)
        self.assertEqual("common", t.getType())

        t = Triangle(-5, -5, -5)
        self.assertEqual("not triangle", t.getType())
        t = Triangle(5, 5, 0)
        self.assertEqual("not triangle", t.getType())
        t = Triangle(0, 0, 0)
        self.assertEqual("not triangle", t.getType())
        t = Triangle(2, 2, 10)
        self.assertEqual("not triangle", t.getType())

        t = Triangle(1, 1, 1)
        self.assertEqual("equilateral", t.getType())

        t = Triangle(4, 4, 6)
        self.assertEqual("isosceles", t.getType())
        t = Triangle(4, 6, 4)
        self.assertEqual("isosceles", t.getType())
        t = Triangle(6, 4, 4)
        self.assertEqual("isosceles", t.getType())

        t = Triangle(3, 4, 5)
        self.assertEqual("right", t.getType())
        t = Triangle(4, 3, 5)
        self.assertEqual("right", t.getType())
        t = Triangle(5, 3, 4)
        self.assertEqual("right", t.getType())

if __name__ == '__main__':
    unittest.main()