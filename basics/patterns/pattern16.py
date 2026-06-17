def pattern(num):
	for i in range(0, num):
		for j in range(i+1):
			print(chr(65+i), end = "")
		print()
num = int(input())
pattern(num)