from typing import MutableSequence
import bisect

def insertion_sort(a: MutableSequence) -> None:
  n = len(a)
  for i in range(1, n):
    j = i
    tmp = a[i]
    # 종료 조건 1: 정렬된 배열의 왼쪽 끝에 도달한 경우 
    # 종료 조건 2: tmp보다 작거나 같은 경우
    while j > 0 and a[j - 1] > tmp:
      a[j] = a[j - 1]
      j -= 1
    a[j] = tmp

def binary_insertion_sort(a: MutableSequence) -> None:
  for i in range(1, len(a)):
    bisect.insort(a, a.pop(i), 0, i)