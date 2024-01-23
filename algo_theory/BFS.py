"""
백준 1926번 문제

 1. 아이디어
 - 2중 for => 값 1 &&  방문 안한 곳
 - BFS 돌면서 그림 개수 +1, 최대값 갱신

 2. 시간복잡도
 - BFS: O(V+E)
 - V: m*n
 - E: V*4
 - O(V+E) = O(m*n + 4*m*n) = O(5*m*n)
 - 계산된 시간복잡도가 2억 이하이므로, 1초 안에 해결 가능

 3. 자료구조
    - 그래프 전체 지도: int[][]
    - 방문 여부: boolean[][]
    - BFS 큐: Queue<int[]>
"""

# 입출력이 빠르게 도와주는 라이브러리
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
map=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]


dy=[-1,1,0,0]
dx=[0,0,-1,1]

def bfs(y,x):
    rs=1    # 그림 크기
    q=[(y,x)]
    while q:
        ey,ex=q.pop()
        for i in range(4):
            ny=ey+dy[i]
            nx=ex+dx[i]
            if 0<=ny<n and 0<=nx<m and map[ny][nx]==1 and visited[ny][nx]==False:
                rs+=1
                visited[ny][nx]=True
                q.append([ny,nx])
    return rs

cnt=0
maxv=0
for j in range(n):
    for i in range(m):
        if map[j][i]==1 and visited[j][i]==False:
            visited[j][i]=True
            # 전체 그림 갯수 +1
            cnt+=1
            # BFS -> 그림 크기
            # 최대값 갱신
            maxv=max(maxv,bfs(j,i))

print(cnt)
print(maxv)
