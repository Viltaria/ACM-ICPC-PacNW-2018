# trevin

import math

n, s = raw_input().split(' ')
n = int(n)
s = int(s)

times = raw_input().split(' ')

times = [int(t) for t in times]

largest_time = max(times)

x = int(largest_time) * s
y = math.ceil(float(x) / float(1000))
print int(y)
