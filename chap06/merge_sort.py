from typing import Sequence, MutableSequence

def merged_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
  pa, pb, pc = 0, 0, 0
  na, nb, nc = len(a), len(b), len(c)

  while pa < na and pb < nb:
    if a[pa] <= b[pb]:
      c[pc] = a[pa]
      pa += 1
    else:
      c[pc] = b[pb]
      pb += 1
    pc += 1

  while pa < na: # a에 남은 원소를 c에 복사
    c[pc] = a[pa]
    pa += 1
    pc += 1

  while pb < nb:
    c[pc] = b[pb]
    pb += 1
    pc += 1

# 방법 2: c = list(sorted(a + b)) -> a와 b를 연결하여 오름차순으로 정렬한 것을 list로 변환하여 c에 저장
# 방법 3: c = list(heapq.merge(a, b)) -> 배열 a와 b를 병합하여 c에 저장, 2에 비해 속도가 더 빠름

def merge_sort(a: MutableSequence) -> None:
  def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
    # a[left] ~ a[right]를 재귀적으로 병합 정렬
    if left < right:
      center = (left + right) // 2
      _merge_sort(a, left, center)
      _merge_sort(a, center + 1, right)

      p = j = 0
      i = k = left

      while i <= center:
        buff[p] = a[i]
        p += 1
        i += 1

      while i <= right and j < p:
        if buff[j] <= a[i]:
          a[k] = buff[j]
          j += 1
        else:
          a[k] = a[i]
          i += 1
        k += 1
      
      while j < p:
        a[k] = buff[j]
        k += 1
        j += 1

  n = len(a)
  buff = [None] * n 
  _merge_sort(a, 0, n - 1)
  del buff     

if __name__ == '__main__':
  print('병합합 정렬을 수행합니다.')
  num = int(input('원소 수를 입력하세요.: '))
  x = [None] * num

  for i in range(num):
    x[i] = int(input(f'x[{i}]: '))
  
  merge_sort(x)

  print('오름차순으로 정렬했습니다.')
  for i in range(num):
    print(f'x[{i}] = {x[i]}')