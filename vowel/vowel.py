vowels = "aeiou"
example = str(raw_input('input a string'))
a = []
for i in example:
	if i.lower() in vowels:
		a.append(i)
print a
count = 0
ecount = 0
icount = 0
ocount = 0
ucount = 0
for item in a:
	if item == 'a':
		count += 1
	elif item == 'e':
		ecount += 1
	elif item == 'i':
		icount += 1
	elif item == 'o':
		ocount += 1
	else:
		ucount += 1
	

print 'a',count
print 'e',ecount
print 'i',icount
print 'o',ocount
print 'u',ucount

