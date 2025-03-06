from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
  n = len(a)
  k = 0

  while k < n - 1:
    last = n - 1
    for j in range(n - 1, k, -1):
      if a[j] < a[j - 1]:
        a[j], a[j - 1] = a[j - 1], a[j]
        last = j
    k = last

  # for i in range(n - 1):
  #   # 패스: 비교 및 교환하는 과정
  #   exchng = 0 # 교환 횟수
  #   for j in range(n - 1, i, -1):
  #     if a[j] < a[j - 1]:
  #       a[j], a[j - 1] = a[j - 1], a[j]
  #     exchng += 1
  #   if exchng == 0:
  #     break # 교환이 일어나지 않음 -> 정렬이 완료됨

if __name__ == '__main__':
  print('버블 정렬을 수행합니다.')
  num = int(input('원소 수를 입력하세요.: '))
  x = [None] * num

  for i in range(num):
    x[i] = int(input(f'x[{i}]: '))
  
  bubble_sort(x)

  print('오름차순으로 정렬했습니다.')
  for i in range(num):
    print(f'x[{i}] = {x[i]}')