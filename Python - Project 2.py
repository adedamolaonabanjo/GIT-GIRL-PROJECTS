Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list_a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> print(list_a)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> list_b = []
>>> for list in list_a:
	if list % 2 == 0:
		list_b.append(list)
		list_b.sort()
		print(list_b)

		
[4]
[4, 16]
[4, 16, 36]
[4, 16, 36, 64]
[4, 16, 36, 64, 100]
>>> 
