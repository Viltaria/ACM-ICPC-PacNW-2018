# Repeating Goldbachs

## Solution Mindset

We can solve this problem by:

1. Generating/Memoizing all the prime numbers up to `x`
2. Working our way inwards using two index pointers `i` and `j` to keep track of where we are, we can check if our memoized numbers at indices `i` and `j` are greater/less than our expected `x`, and either subtract j or increment i respectively
3. This continues until our `x < 4` condition is satisfied, updating the value of `x` with the memoized number at index `j` subtracted by the memoized number at index `i` (_q - p_)
