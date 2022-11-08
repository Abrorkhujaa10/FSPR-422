def fen(n):
    if n in (1, 2):
        return 1
    return fen(n - 1) + fen(n - 2)
print(fen(6))


a = [
    [0, 2, 4, 7],
    [1, 4, 6, 8],
    [3, 5, 9, 1]
]
for i in a:
    print(i)