from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
  def __init__(self, key: Any, value: Any, next: Node) -> None:
    self.key = key
    self.value = value
    self.next = next
  
class ChainedHash:
  def __init__(self, capacity: int) -> None:
    self.capacity = capacity
    self.table = [None] * self.capacity # 해시 테이블 선언

  def hash_value(self, key: Any) -> int:
    if isinstance(key, int):
      return key % self.capacity # key가 int형인 경우
    # key가 int형이 아닌 경우
    return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
  
  def search(self, key: Any) -> Any:
    hash = self.hash_value(key)
    p = self.table[hash]

    while p is not None:
      if p.key == key:
        return p.value
      p = p.next

    return None
  
  def add(self, key: Any, value: Any) -> bool:
    hash = self.hash_value(key)
    p = self.table[hash]

    while p is not None:
      if p.key == key:
        return False
      p = p.next

    temp = Node(key, value, self.table[hash]) # 새 노드를 만들고 기존 첫 번째 노드를 next로 연결
    self.table[hash] = temp # 새 노드를 버킷의 첫 번째 노드로 설정
    return True
  
  def remove(self, key: Any) -> bool:
    hash = self.hash_value(key)
    p = self.table[hash]
    pp = None

    while p is not None:
      if p.key == key:
        if pp is None:
          self.table[hash] = p.next
        else:
          pp.next = p.next
        return True
      pp = p
      p = p.next
    return False
  
  # 원소 출력 
  def dump(self) -> None:
    for i in range(self.capacity):
      p = self.table[i]
      print(i, end='')
      while p is not None:
        print(f'  -> {p.key} ({p.value})', end='')
        p = p.next
      print()