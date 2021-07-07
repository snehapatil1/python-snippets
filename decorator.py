
def mydecorator(fn):

	def function_wrapper():
		print(f'Before calling - {fn.__name__}')
		fn()
		print(f'After calling - {fn.__name__}')

	return function_wrapper

@mydecorator
def foo():
	name = input("Enter your name:  ")
	print(f'Hi {name}! Nice to meet you.')


foo()