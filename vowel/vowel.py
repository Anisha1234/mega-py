vowels = "aeiou"
example = "my name is anisha"
a = []
for i in example:
	if i.lower() in vowels:
		a.append(i)
print a


