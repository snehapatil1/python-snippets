
def bubble_sort(_list):
	for passnum in range(len(_list) - 1, 0, -1):
		for i in range(passnum):
			if _list[i] > _list[i + 1]:
				temp = _list[i]
				_list[i] = _list[i + 1]
				_list[i + 1] = temp

_list = [54,26,93,17,77,31,44,55,20]
print(f'Original List: {_list}\n')

bubble_sort(_list)
print(f'Sorted List: {_list}\n') # [17,20,26,31,44,54,55,77,93]