n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False] * n for _ in range(n)]
start = ()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            start = (i,j)
            break
    if start:
        break
stack = []
stack.append(start)
# print(stack)
count = 0
people = [0] * (n*n)
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            count += 1 # 마을 갯수 세기
            cnt_people = 0
            # is_only = False
            people[count] = 1
            stack.append((i,j))
            while stack:
                x, y = stack.pop()
                for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx,ny))
                        cnt_people += 1
                        # is_only = False
                if cnt_people:
                    people[count] = cnt_people
                

answer = []
for i in range(len(people)):
    if people[i] != 0:
        answer.append(people[i])
# print(count, answer)
answer.sort()
print(count)
for i in range(len(answer)):
    print(answer[i])