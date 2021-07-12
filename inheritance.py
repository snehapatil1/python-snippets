
class Shape:
	def __init__(self):
		print('-'*10)
		print('Shape')
		print('-'*10+'')

class Polygon(Shape):
	def __init__(self):
		super().__init__()
		print('\n\tPolygon')

class Rectangle(Polygon):
	def __init__(self):
		super().__init__()
		print('\n\tRectangle')

class Triangle(Polygon):
	def __init__(self):
		super().__init__()
		print('\n\tTriangle')

class Square(Rectangle):
	def __init__(self):
		super().__init__()
		print('\n\tSquare')

class Ellipse(Shape):
	def __init__(self):
		super().__init__()
		print('\n\tEllipse')

class Circle(Ellipse):
	def __init__(self):
		super().__init__()
		print('\n\tCircle')

polygon = Polygon()
rectangle = Rectangle()
triangle = Triangle()
square = Square()
ellipse = Ellipse()
circle = Circle()