from typing import MutableSequence

def counting_sort(a: MutableSequence) -> None:
  max = max(a)

  n = len(a)  # 정렬할 배열 a
  f = [0] * (max + 1) # 누적 도수 분포표 배열 f
  b = [0] * n # 작업용 배열 b

  # 1단계: 도수 분포표 만들기
  for i in range(n):    
    f[a[i]] += 1

  # 2단계: 누적 도수 분포표 만들기
  for i in range(1, max + 1):
    f[i] += f[i - 1]

  # 3단계: 작업용 배열 만들기
  for i in range(n - 1, -1, -1):
    f[a[i]] -= 1; b[f[a[i]]] = a[i]

  # 4단계: 배열 복사하기
  for i in range(n):
    a[i] = b[i]
