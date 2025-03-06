# # 방법 1: 가장 일반적인 방법법
# counter = 0

# for n in range(2, 1001):
#   for i in range(2, n):
#     counter += 1
#     if n % i == 0: break
#   else: # for문이 끝까지 실행됐을 경우 else문이 실행됨
#     print(n)

# print(f'나눗셈을 실행한 횟수: {counter}') # 78022


# # 방법 2: 소수로 나누어 떨어지지 않는 지만 판단하면 됨
# counter = 0
# ptr = 0
# prime = [None] * 500

# prime[ptr] = 2
# ptr += 1

# for n in range(3, 1001, 2): # 홀수만 대상으로 설정 -> 2로는 나누지 않는다.
#   for i in range(1, ptr):
#     counter += 1
#     if n % prime[i] == 0: break
#   else:
#     prime[ptr] = n # 소수로 배열에 등록
#     ptr += 1

# for i in range(ptr):
#   print(prime[i])

# print(f'나눗셈을 실행한 횟수: {counter}') # 14622

# 방법 3: 특정 수의 제곱근이 소수로 나누어 떨어지지 않는 지만 판단하면 됨
counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
  i = 1
  while prime[i] * prime[i] <= n:
    counter += 2 # 곱셈과 나눗셈 두 가지 연산을 수행
    if n % prime[i] == 0: break
    i += 1
  else:
    prime[ptr] = n
    ptr += 1
    counter += 1 # while문의 조건(곱셈) 만족 x -> 1만 증가

for i in range(ptr):
  print(prime[i])

print(f'나눗셈을 실행한 횟수: {counter}') # 3774