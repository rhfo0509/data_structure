# 유클리드 호제법으로 gcd 구하기
# 나눗셈을 반복하면서 나머지가 0이 될 때까지 계산하는 방식

def gcd(x: int, y: int) -> int:
  if y == 0:
    return x
  else:
    return gcd(y, x % y)