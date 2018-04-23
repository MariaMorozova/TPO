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
		a = self.triangle[0]
		b = self.triangle[1]
		c = self.triangle[2]
		
		p = (a+b+c)
		p = p/2.0
		S = math.sqrt(p*(p-a)*(p-b)*(p-c))
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
			adj1 = c
			opp = b
		elif (angle == 'gamma'):
			adj1 = a
			adj2 = b
			opp = c
		else:
			return False
	
		f = (adj1**2 + adj2*2 - opp**2)/(2.0*adj1*adj2)
		return math.degrees(math.acos(f))
	
	def isTriangle(self):
		'''
			Проверка, что треугольник с введенными сторонами вообще может существовать
		'''
		fail = False
		a = self.triangle[0]
		b = self.triangle[1]
		c = self.triangle[2]
		
		if (a <= 0):
			fail = True
		elif (b <= 0):
			fail = True
		elif (c <= 0):
			fail = True
		
		if (a >= b+c):
			fail = True
		elif (b >= a+c):
			fail = True
		elif (c > a+b):
			fail = True
		
		if (fail):
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
		
		if ((a == b) and (a == c)):
			type = 'equilateral'
		elif (a == b) and (a != c):
			type = 'isosceles'
		elif (a == c) and (a != b):
			type = 'isosceles'
		elif (b == c) and (b != a):
			type = 'isosceles'
	
		if (a**2 == b**2 + c**2):
			type = 'right'
		elif (b*2 == a**2 + c**2):
			type = 'right'
		elif (c**2 == a**2 + b**2):
			type = 'right'
	
		return type


class TriangleTest(unittest.TestCase):
	def setUp(self):
		print "Test started"
		
	def tearDown(self):
		print "Test finished"

	# Проверяем, что на корректных значениях программа работает
	def testIsTriangle(self):
		t = Triangle(2, 3, 4)
		self.assertTrue(t.isTriangle())
		
	# значение некорректное, это не треугольник, функция isTriangle() должна вернуть false
	def testIsNotTriangle(self):
		t = Triangle(2, 3, 5)
		self.assertFalse(t.isTriangle())
		
if __name__ == '__main__':
	unittest.main()
	