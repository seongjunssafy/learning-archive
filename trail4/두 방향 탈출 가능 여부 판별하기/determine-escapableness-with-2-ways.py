n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False] * m for _ in range(n)]

visited[0][0] = True

def dfs(x,y):
    for dx, dy in [[1,0], [0,1]]:
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
            visited[nx][ny] = True
            dfs(nx, ny)

dfs(0,0)

print(int(visited[n-1][m-1]))