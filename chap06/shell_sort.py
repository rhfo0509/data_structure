from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
  n = len(a)
  gap = n // 2
  while gap > 0:
    # gap만큼 떨어진 요소들을 삽입 정렬
    for i in range(gap, n):
      tmp = a[i]
      j = i
      while j >= gap and a[j - gap] > tmp:
        a[j] = a[j - gap]
        j -= gap
      a[j] = tmp
    gap //= 2
