from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
  n = len(a)
  for i in range(n // 2):
    a[i], a[n - i - 1] = a[n - i - 1], a[i]

if __name__ == '__main__':
  print('배열 원소를 역순으로 정렬합니다.')
  nx = int(input('원소 수를 입력하세요: '))
  x = [None] * nx

  for i in range(nx):
    x[i] = int(input(f'x[{i}]값을 입력하세요: '))

  reverse_array(x)

  print('배열 원소를 역순으로 정렬했습니다.')
  for i in range(nx):
    print(f'x[{i}] = {x[i]}')

# x.reverse() : 리스트 자기 자신을 역순으로 정렬
# list(reversed(x)) : 역순으로 정렬된 새 리스트 생성