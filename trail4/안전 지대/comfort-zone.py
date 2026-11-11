n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
k = 1
answer = []
while k <= max(max(row) for row in grid):
    count = 0
    stack = []
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] > k and not visited[i][j]:
                count += 1 # 안전지대 갯수 세기
                stack.append((i,j))
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > k and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
    answer.append((count, k))
    k+=1
# print(answer)
answer.sort(key=lambda x: (-x[0], x[1]))
if answer[0][0] == 0:
    print(1, 0)
else:
    print(answer[0][1], answer[0][0])