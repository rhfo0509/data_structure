# 링 버퍼의 활용
# 가장 최근에 들어온 데이터 n개만 저장하고 나머지 오래된 데이터는 버림

n = int(input('정수를 몇 개 저장할까요?: '))
a = [None] * n

cnt = 0
while True:
  a[cnt % n] = int(input(f'{cnt + 1}번째 정수를 입력하세요.: '))
  cnt += 1

  retry = input(f'계속 할까요?(Y/N): ')
  if retry in {'N', 'n'}:
    break

# n이 10이고 cnt가 12인 경우 a[2]부터 출력해야 함
start = cnt - n
for i, value in enumerate(a, start):
  print(f'{i}번째 = {value}')
# for i in range(n):
#   print(f'{cnt - n + i}번째 = {a[(cnt - n + i) % n]}')