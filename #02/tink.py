import string

print("hell yeah")

with open("mess.txt") as fp:
	content = fp.read()
	lis_t = [int(val) for val in content.split()]
	print(lis_t)
	for each in lis_t:
		mod = each % 37
		if mod in range (26):
			print(string.ascii_uppercase[mod])
		elif mod in range (26,36):
			print(string.digits[mod - 26])
		else:
			print(mod)
		