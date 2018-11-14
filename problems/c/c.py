def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    bad = {}
    valid = True
    for i in range(0, len(indices)):
      if pool[indices[i]] in bad:
        valid = False
        break
      else:
        bad[pool[indices[i]]] = 1
    if valid:
      yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        bad = {}
        valid = True
        for i in range(0, len(indices)):
          if pool[indices[i]] in bad:
            valid = False
            break
          else:
            bad[pool[indices[i]]] = 1
        if valid:
          yield tuple(pool[i] for i in indices)

n, k = raw_input().split(' ')
difficulty = raw_input().split(' ')

cs = list(combinations(difficulty, int(k)))

amount = len(cs)
print amount
