def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y):
    if not in_range(x, y):
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [
    list(map(int, sys.stdin.readline().rstrip()))
    for _ in range(n)
]

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1


print(result)