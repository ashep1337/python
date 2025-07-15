n = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(n)):
    if n[i] > 6 and sum(n) > 10:
        n[i] = 1

print(n)
