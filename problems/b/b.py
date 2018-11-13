from fractions import gcd

a, b, c, d = raw_input().split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)

mem = {}
done_numbers = set()

count = 0

for i in range(a, b + 1):
  for j in range(c, d + 1):
    if j in done_numbers:
      pass
    if (str(j) + " " + str(i)) in mem:
      result = mem[str(j) + " " + str(i)]
    else:
      result = gcd(i, j)
      mem[str(i) + " " + str(j)] = result
    if result == 1:
	count += 1
  done_numbers.add(i)

print count
