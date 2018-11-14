import math
k, b = raw_input().split(' ')

k = int(k)
b = int(b)

numbits = 0
cap = (math.pow(2, b) - 1) % 1000000009

i = 1
multiple = k * i

while multiple <= cap:
  for x in range(0, 32):
    numbits += (multiple >> x) & 1
  i += 1
  multiple = k * i
print numbits
