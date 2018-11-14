k = int(raw_input())
my_answers = raw_input()
friend_answers = raw_input()
n = len(my_answers)

same = n - sum(1 for a, b in zip(my_answers, friend_answers) if a != b) # Count similarities between the two strings

x = abs(same - k)
print n - x
