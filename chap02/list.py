x = ['John', 'George', 'Paul', 'Ringo']

# 리스트의 모든 원소를 enumerate() 함수로 스캔하기 (1부터 카운트)
for i, name in enumerate(x, 1):
  print(f'{i}번째 = {name}')

# 리스트의 모든 원소를 스캔하기(인덱스값 x)
for i in x:
  print(i)