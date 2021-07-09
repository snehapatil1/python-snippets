
class TestCallable:
	def main(self, value=None):
		output = value() if callable(value) else value
		print(f'Value is: {output}')

testobj = TestCallable()

# Value (Non-callable)
testobj.main(100)

# Function (Callable)
testfn = lambda x: x*100
testobj.main(testfn(20))





