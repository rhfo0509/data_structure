# 재귀 알고리즘

# def recur(n: int) -> int:
#   if n > 0:
#     recur(n - 1)
#     print(n)
#     recur(n - 2)

# 꼬리 재귀 제거
# recur(n - 2) == n - 2로 업데이트하고 함수의 시작 지점으로 돌아간다

# def recur(n: int) -> int:
#   while n > 0:
#     recur(n - 1)
#     print(n)
#     n = n - 2

# 재귀 제거
# recur(n - 1) != n - 1로 업데이트하고 함수의 시작 지점으로 돌아간다
# 스택을 통해 해결

from collections import deque
def recur(n: int) -> int:
  s = deque([], n)

  while True:
    if n > 0:
      s.append(n)
      n = n - 1
      continue
    if len(s):
      n = s.pop()
      print(n)
      n = n - 2
      continue
    break

x = int(input('정숫값을 입력하세요.: '))

recur(x)