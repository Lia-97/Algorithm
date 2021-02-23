# 파스칼의 삼각형
# T= int(input())
# for tc in range(1, T+1):
#     # 첫번째 줄과 두번째 줄은 주어져 있음
#     pascal = [[1], [1, 1]]
#     N = int(input())
#     for i in range(2, N):
#         # pascal 에 append 할 arr 리스트를 생성한다. arr 리스트의 첫번째 원소는 1.
#         arr= [1]
#         for j in range(i-1):
#             # 구하고자 하는 원소(리스트)의 하나 전 리스트의 원소들의 합이 새로 추가하는 리스트의 원소가 된다.
#             arr.append(pascal[i-1][j] + pascal[i-1][j+1])
#         arr.append(1) # arr 리스트의 마지막 원소도 1.
#         pascal.append(arr) # pascal 리스트에 arr 을 더한다.
#
#     # N 이 1이면 pascal 의 첫번째 원소만 출력할 수 있게 조정해준다.
#     if N == 1:
#         pascal = pascal[:N]
#
#     print('#{}'.format(tc))
#     for p in pascal:
#         p = map(str, p)
#         p = ' '.join(p)
#         print(p)

# 부분집합 재귀로 풀어보기 _ 원재한테 물어보기
# def recur(n, k):
#     if n == k:
#         print(bit) # 전체 부분집합 출력
#         for i in range(k):
#             if bit[i]:
#                 print(A[i], end = ' ')
#         print()
#         return
#     else:
#         bit[n] = 0
#         recur(n+1, k)
#         bit[n] = 1
#         recur(n+1, k)
#
# A = [10, 20, 30]
# N = len(A)
# bit = [0] * N
# recur(0, N) # 0번 원소부터 복사, 원소의 수 N개

# 음료수 얼려 먹기 _ 미완
# N, M = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]
# print(arr)
#
# def ice(x, y):
#     if x < 0 or x >= M or y < 0 or y >= N:
#         return False
#     if arr[x][y] == 0:
#         pass

# 반복문자 지우기
# T = int(input())
# for tc in range(1, T+1):
#     lis = list(map(str, input()))
#     stack = [-1] # 인덱스 에러를 방지하기 위해 임의의 원소 -1 넣어줌.
#
#     # lis 의 길이가 0이 아닌동안
#     while len(lis)!= 0:
#         # lis 의 가장 마지막 값이 stack 의 가장 마지막 값과 같은지 비교햔다.
#         last = lis.pop()
#         # 같으면 stack 에서도 해당 값을 빼주고
#         if last == stack[-1]:
#             stack.pop()
#         # 다르면 더해준다.
#         else:
#             stack.append(last)
#
#     # stack 생성 시, 임의로 넣었던 값 -1 은 제외해 줘야 하므로 len(stack)-1
#     ans = len(stack)-1
#     print('#{} {}'.format(tc, ans))

# 괄호검사
# T = int(input())
# for tc in range(1, T+1):
#     lis = list(map(str, input()))
#     # 각 괄호에 해당하는 숫자를 지정한다. 짝이 되는 괄호의 합이 0 이 되도록.
#     dic = {'(': 1, ')': -1, '{': 2, '}': -2, '*': 0}
#     # 맨 처음 들어올 값과 비교하기 위해 임의의 값을 넣어놓는다.
#     stack = ['*']
#     while len(lis) > 0:
#         last = lis.pop()
#         # lis 의 마지막 원소가 괄호 4종에 해당한다면
#         if last in ['(',')','{','}']:
#             # 딕셔너리에서 해당 괄호의 숫자를 가져와서 stack 의 원소가 해당하는 숫자와 합이 0인지 확인한다.
#             if dic.get(stack[-1]) + dic.get(last) == 0:
#                 # 합이 0이면 짝을 이룬다는 뜻이므로 stack 에서 pop
#                 stack.pop()
#             # 합이 0이 되지 않는다면 append
#             else:
#                 stack.append(last)
#     # 모든 괄호가 짝을 이루었다면 stack 에서 전부 pop 되었을테니까, stack 의 길이는 초기값의 길이인 1이 되어야 함.
#     if len(stack) == 1:
#         ans = 1
#     else:
#         ans = 0
#
#     print('#{} {}'.format(tc,ans))

# 종이 붙이기_???????
# def Paper(N):
#     dp = []
#     N = N // 10
#     dp.append(1)
#     dp.append(3)
#     for i in range(2, N):
#         # (i-1) 왼쪽 끝이 2 x 1 막대, (i-2) 왼쪽 끝이 2 x 2 막대(가로로 2x1 2개 또는 2x2 1개 이므로 * 2)
#         dp.append(dp[i - 1] + dp[i - 2] * 2)
#     return dp[-1]
#
#
# T = int(input())
# for test in range(1, T + 1):
#     N = int(input())
#     print(f'#{test}', Paper(N))

# 그래프 경로
# def f(s, g, v): # s에서 g에 도착할 수 있는지 확인하는 함수
#     # 중복없이 빠짐없이 탐색하는 dfs
#     stack = [] # stack 생성
#     visited = [0]*(v+1) # visited 생성
#     stack.append(s) # push(s) 갈림길 목록에 시작점 추가
#     visited[s] = 1 # visited[s] <= 1 방문예약 표시(중복된 push 방지)
#     while stack: # 스택이 비어있지 않으면(방문할 곳이 남아있으면)
#         n = stack.pop() # 방문할 목록에서 마지막에 기록된 노드를 꺼내
#         if n == g: # 방문할 노드가 목적지 g인지 확인
#             return 1 # 경로가 존재하기 때문
#         for i in range(1, V+1): # 모든 노드에 대해, 현재노드에서 방문할 수 있는 곳인지 검토
#             if adj[n][i] == 1 and visited[i] == 0: # 인접하고 미방문인 노드 i 를 찾으면
#                 stack.append(i) # push(i)
#                 visited[i] = 1
#
#     return 0 # 목적지에 도달하지 못하고, 탐색할 노드가 더 이상 없는 경우
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     adj = [[0] * (V+1) for _ in range(V+1)] # 인접행렬 생성, 초기화
#     for _ in range(E):
#         n1, n2 = map(int, input().split())
#         adj[n1][n2] = 1 # 연결되어있으면 1로 바꿔줌
#         # adj[n2][n1] = 1 # 방향성이 없기 때문
#     S, G = map(int, input().split()) # 출발점, 목적지
#     print('#{} {}'.format(tc, f(S, G, V)))

# 길 찾기 _ 시간 초과 뜸
# def find():
#     stack = []
#     visited = [0]*100
#     stack.append(1)
#     visited[1] = 1
#     while stack:
#         n = stack.pop()
#         if n == 99:
#             return 1
#         for i in range(0, 100):
#             if arr[n][i] == 1 and visited[i] == 0:
#                 stack.append(i)
#                 visited[i] = 1
#     return 0
#
# for tc in range(11):
#     tc, N = map(int, input().split())
#     node = list(map(int, input().split()))
#     arr = [[0] * 100 for _ in range(100)]
#
#     for i in range(N):
#         arr[node[i * 2]][node[i * 2 + 1]] = 1
#
#
#     print('#{} {}'.format(tc, find()))


# 길 찾기 _ 런타임 에러를 없애보자.
for tc in range(11):
    tc, N = map(int, input().split())



