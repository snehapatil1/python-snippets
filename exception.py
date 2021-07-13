
class MyException:
	def divide(self, numerator, denominator):
		try:
			return print(f'Value: {numerator / denominator}')
		except ZeroDivisionError as zero:
			denominator = int(input('Please enter correct value for denominator: '))
			self.divide(numerator, denominator)
	def main(self):
		numerator = int(input(f'Enter Numerator: '))
		denominator = int(input(f'Enter Denominator: '))
		self.divide(numerator, denominator)

obj = MyException()
obj.main()