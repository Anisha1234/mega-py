a = int(raw_input('Give amount: '))

def fib(n):
	b,c = 0,1
	for i in range(n-1):
		b,c = c,c + b 
		print c
 	return c
fib(a)


