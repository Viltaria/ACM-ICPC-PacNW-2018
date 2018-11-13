def SieveOfEratosthenes(n): # Function to calculate/memoize all prime numbers up until "x"
	memoize = {}
	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):
	    if (prime[p] == True):
	        for i in range(p * 2, n+1, p):
	            prime[i] = False
	    p += 1

	i = 0
	for p in range(2, n):
	    if prime[p]:
	        memoize[i] = p
	        i += 1
	return memoize, i - 1

x = int(raw_input())

memoize, j = SieveOfEratosthenes(x) # Generates all prime numbers up to given "x", set "j" as upper index bound
steps = 0 # Count number of Goldbachs

while not x < 4:
	i = 0 # Set initial "i" value to account for all cases
	while memoize[i] + memoize[j] != x:
		# Try and add memoized values at indices "i" and "j" to expected sum "x", adjusting values of "i" and "j" on the way
		if memoize[i] + memoize[j] > x:
			j -= 1
		elif memoize[i] + memoize[j] < x:
			i += 1
	steps += 1
	x = memoize[j] - memoize[i]

print steps
