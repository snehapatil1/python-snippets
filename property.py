
class TestProperty:
	def __init__(self, temp=0):
		self.temp = temp

	@property
	def temp(self):
		print("Getting...")
		return print(self._temp)

	@temp.setter
	def temp(self, value):
		print("Setting...")
		self._temp = value

	def main(self):
		return print(self._temp * 100)

test_obj = TestProperty(20)
test_obj.temp
test_obj.main()