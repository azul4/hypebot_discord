n, m = map(int, input().split())
arr, store = [[0 for _ in range(6)] for _ in range(6)] , [] #나중에 16으로 고치기
visited = [[False for _ in range(6)] for _ in range(6)]
for i in range(1,n+1): 
    arr[i][1:] = list(map(int, input().split()))
for i in range(m):
    li=list(map(int, input().split()))
    store.append(li)
store.insert(0, None)
t=0
loc = [[None, None] for _ in range(m+1)] #현재 좌표
#베이스캠프 좌표 뽑기
bc_list=[]
for i in range(6): #나중에 16으로 고치기
    for j in range(6):
        if arr[i][j] == 1:
            bc_list.append([i,j])

### utilities
def dist(a:list, b:list):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

### debugging
def printmap():
    print("map")
    for i in arr:
        print(i)
    print("visited")
    for i in visited:
        print(i)

### simulation
def phase1(nt): # 최단거리로만 이동하고, 우선순위는 상좌우하
    '''
    격자에 있는 사람들이 본인이 가고 싶은 편의점 방향을 향해서 1 칸 움직입니다. 
    최단거리로 움직이며 최단 거리로 움직이는 방법이 여러가지라면 ↑, ←, →, ↓ 의 우선 순위로 움직이게 됩니다. 
    여기서 최단거리라 함은 상하좌우 인접한 칸 중 이동가능한 칸으로만 이동하여 도달하기까지 거쳐야 하는 칸의 수가 최소가 되는 거리를 뜻합니다.
    '''

    dr = [-1,0,0,1]
    dc = [0,-1,1,0]

    def movable(nr, nc):
        if visited[nr][nc]: return False
        if 1<nr<=n and 1<nc<=n: return True
        else: return False

    """
    #dfs로 구할 게 아니었음

    def dfs(nr, nc, length): #상좌우하 순서로 거리 구하기
        if arr[nr][nc] == store[t]:
            return 1
        
        for i in range(4):
            nnr, nnc = nr+dr[i], nc+dc[i]
            if movable(nnr, nnc):
                dfs_visited[nr][nc]=True
                dfs(nnr, nnc, length+1)
                dfs_visited[nr][nc]=False
    """
    bfs_visited = [[False for _ in range(6)] for _ in range(6)]
    def bfs(r,c):
        from collections import deque
        q=deque()
        length = 1
        min_length = 999999999999
        bfs_visited[r][c] = True
        q.push([r,c,length])
        while not q.empty():
            r, c, length = q.popleft()
            nr, nc = r+dr[i], c+dc[i]
            if bfs_visited[nr][nc]: continue
            if 1<nr<=n and 1<nc<=n:
                bfs_visited[nr][nc]=True
                q.append([nr,nc, length+1])

            #편의점 도착할 때만 거리 집계
            if arr[nr][nc] == loc[t]:
                _, _, length = q.pop()
                min_length = min(length, min_length)
        return min_length

    #최단거리를 가리키는 방향 구하기 (그 순간의 최단거리인가? 결과론적으로 최단거리인가?)
    #사람이 격자에 있는지 판단 먼저 필요
    for it in range(1, t):
        r,c = loc[it][0], loc[it][1]
        d=[]
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if movable(nr,nc): 
                d.append(bfs(nr, nc, 1)) #상좌우하 순서로 거리 구해짐
        direction = d.index(min(d))

        #그쪽으로 움직이기
        nr, nc = r+dr[direction], c+dc[direction]
        loc[t] = [nr,nc]

def phase2(): # 편의점 먹으면 그 칸으로 아무도 못감
    """
    만약 편의점에 도착한다면 해당 편의점에서 멈추게 되고, 이때부터 다른 사람들은 해당 편의점이 있는 칸을 지나갈 수 없게 됩니다.
    """

    #편의점 도착했으면 그 칸 visited처리
    for t in range(1, m+1):
        if loc[t] == store[t]:
            r,c = loc[t][0], loc[t][1]
            visited[r][c] = True


def phase3(t): 
    '''
    t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어갑니다. 
    여기서 가장 가까이에 있다는 뜻 역시 1에서와 같이 최단거리에 해당하는 곳을 의미합니다. 
    가장 가까운 베이스캠프가 여러 가지인 경우에는 그 중 행이 작은 베이스캠프, 행이 같다면 열이 작은 베이스 캠프로 들어갑니다. 
    t번 사람이 베이스 캠프로 이동하는 데에는 시간이 전혀 소요되지 않습니다.
    '''
    #가고싶은 편의점과 가장 가까운 베이스캠프 리스트에 담기
    min_dist, min_bc_list = 999999999, []
    for bc in bc_list:
        cur_dist = dist(bc, loc[t]) #1번사람 최단거리 구하기 
        #print(cur_dist)
        if cur_dist <= min_dist: 
            min_dist = cur_dist
            min_bc_list.append(bc)
    #print(f"min_bc_list={min_bc_list}")    

    #그 리스트 중 행작은거/열작은거 선택하기
    temp=[]
    for i in min_bc_list:
        temp.append(i[0]*20+i[1])
    min_temp = min(temp)
    idx = temp.index(min_temp)
    r, c = min_bc_list[idx][0], min_bc_list[idx][1]
    visited[r][c] = True # 선택된 베이스캠프는 앞으로 지나갈 수 없음
    loc[t] = [r,c] # t번째 사람의 현위치는 최단거리에 해당하는 베이스캠프
    #print(f'loc={loc}')

while True:
    t+=1
    phase1(t) #t-1초의 사람만이 격자에 존재함
    phase2()
    if t<=m: phase3(t)
    printmap()
    break
print(t)