from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

class Status(Enum):
  OCCUPIED = 0
  EMPTY = 1
  DELETED = 2

class Bucket:
  def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
    self.key = key
    self.value = value
    self.stat = stat

  def set(self, key: Any, value: Any, stat: Status) -> None:
    self.key = key
    self.value = value
    self.stat = stat

  def set_status(self, stat: Status) -> None:
    self.stat = stat

class OpenHash:
  def __init__(self, capacity: int) -> None:
    self.capacity = capacity
    self.table = [Bucket()] * self.capacity

  def hash_value(self, key: Any) -> int:
    if isinstance(key, int):
      return key % self.capacity # key가 int형인 경우
    # key가 int형이 아닌 경우
    return (int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)
  
  def rehash_value(self, key: Any) -> int:
    return (self.hash_value(key) + 1) % self.capacity # 다음 인덱스의 버킷을 확인
  
  def search_node(self, key: Any) -> Any:
    hash = self.hash_value(key)
    p = self.table[hash]

    for i in range(self.capacity):
      if p.stat == Status.EMPTY:
        break
      elif p.stat == Status.OCCUPIED and p.key == key:
        return p
      # 현재 버킷이 DELETED이거나, OCCUPIED지만 키가 다른 경우
      hash = self.rehash_value(hash)
      p = self.table[hash]
    return None
  
  def search(self, key: Any) -> Any:
    p = self.search_node(key)
    if p is not None:
      return p.value
    else:
      return None
    
  def add(self, key: Any, value: Any) -> bool:
    if self.search(key) is not None:
      return False # 이미 등록된 키
    
    hash = self.hash_value(key)
    p = self.table[hash]
    for i in range(self.capacity):
      if p.stat == Status.DELETED or p.stat == Status.EMPTY:
        self.table[hash] = Bucket(key, value, Status.OCCUPIED)
        return True
      hash = self.rehash_value(key)
      p = self.table[hash]
    return False # 해시 테이블이 가득 참
  
  def remove(self, key: Any) -> bool:
    p = self.search_node(key)
    if p is None:
      return False
    p.set_status(Status.DELETED)
    return True
  
  def dump(self) -> None:
    for i in range(self.capacity):
      print(f'{i:2} ', end='')
      if self.table[i].stat == Status.OCCUPIED:
        print(f'{self.table[i].key} ({self.table[i].value})')
      elif self.table[i].stat == Status.EMPTY:
        print('-- 미등록 --')
      elif self.table[i].stat == Status.DELETED:
        print('-- 삭제 완료 --')