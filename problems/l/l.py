n = int(raw_input())

lines = [raw_input().split(' ') for i in range(0, n)] # Read in "n" number of lines

claims = [0] * n # Initialize claims to 0 for simple addition

for l in lines: # For each input line "l", loop from the first to second number to figure out the number of claims for each person
	low = int(l[0])
	high = int(l[1])
	for i in range(low, high + 1):
		claims[i - 1] += 1

for i, c in reversed(list(enumerate(claims))): # Loop over all the claims from back to front
	if c == i + 1: # If the number of people matches the number of claims, print "c" and exit
		print c
		exit()
print -1
