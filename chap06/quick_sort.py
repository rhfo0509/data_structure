from typing import MutableSequence

def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
  if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
  if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
  if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
  return idx2

def qsort(a: MutableSequence, left: int, right: int) -> None:
  pl = left
  pr = right
  # x = a[(left + right) // 2]
  
  m = sort3(a, pl, (pl + pr) // 2, pr) # new pivot
  x = a[m]
  a[m], a[pr - 1] = a[pr - 1], a[m]
  pl += 1
  pr -= 2

  while pl <= pr:
    while a[pl] < x: pl += 1
    while a[pr] > x: pr -= 1
    if pl <= pr:
      a[pl], a[pr] = a[pr], a[pl]
      pl += 1
      pr -= 1

  # 분할 정복 알고리즘 - 재귀 호출을 사용하여 구현 
  if left < pr: qsort(a, left, pr)
  if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
  qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
  print('퀵 정렬을 수행합니다.')
  num = int(input('원소 수를 입력하세요.: '))
  x = [None] * num

  for i in range(num):
    x[i] = int(input(f'x[{i}]: '))
  
  quick_sort(x)

  print('오름차순으로 정렬했습니다.')
  for i in range(num):
    print(f'x[{i}] = {x[i]}')
