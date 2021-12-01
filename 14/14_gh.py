n = 652601

def step(scores, i, j):
    # sum the current scores
    s = scores[i] + scores[j]
    # the sum will be at most 9 + 9 = 18, so we can just check for a leading 1
    if s >= 10:
        scores.append(1)
    scores.append(s % 10)
    # move the elves to their new positions
    i = (i + scores[i] + 1) % len(scores)
    j = (j + scores[j] + 1) % len(scores)
    return (i, j)

# part 1
scores, i, j = [3, 7], 0, 1 # initial condition
# loop until we've scored enough recipes
while len(scores) < n + 10:
    i, j = step(scores, i, j)
# print the 10 scores of interest
print(''.join(map(str, scores[n:n+10])))

# part 2
scores, i, j = [3, 7], 0, 1 # initial condition
# extract the individual digits from our input
digits = list(map(int, str(n)))
while True:
    i, j = step(scores, i, j)
    # check if the last N digits match our input
    # we need to check both the ultimate and penultimate index
    # since we might have added two new recipes in the most recent step
    if scores[-len(digits)-1:-1] == digits:
        print(len(scores) - len(digits) - 1)
        break
    if scores[-len(digits):] == digits:
        print(len(scores) - len(digits))
        break