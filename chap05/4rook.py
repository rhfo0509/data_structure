pos = [0] * 4       # 각 열에서 룩의 위치
flag = [False] * 4  # 각 행에 룩을 배치했는지 체크

def put() -> None:
  for i in range(4):
    print(f'{pos[i]:2}', end='')
  print()

# i열 j행
def set(i: int) -> None:
  for j in range(4):
    if not flag[j]: # j행에 룩을 배치하지 않았으면
      pos[i] = j
      if i == 3:
        put()
      else:
        flag[j] = True
        set(i + 1) # 다음 열에 룩을 배치
        flag[j] = False

set(0)