from typing import Any, Type
from __future__ import annotations

Null = -1

class Node:
  """연결 리스트용 노드 클래스(배열 커서 버전)"""
  def __init__(self, data = Null, next = Null, dnext = Null):
    self.data = data
    self.next = next
    self.dnext = dnext # 프리 리스트의 뒤쪽 포인터터

class LinkedList:
  """연결 리스트 클래스(배열 커서 버전전)"""
  def __init__(self, capacity: int) -> None:
    self.no = 0
    self.head = Null
    self.current = Null
    self.max = Null     # 배열에서 맨 끝 쪽에 저장되는 노드의 레코드 번호
    self.deleted = Null # 프리 리스트의 머리 노드를 참조하는 커서
    self.capacity = capacity # 리스트의 크기
    self.n = [Node()] * self.capacity # 리스트 본체

  def __len__(self) -> int:
    return self.no
  
  def get_insert_index(self):
    """다음에 삽입할 레코드의 인덱스를 구함"""
    if self.deleted == Null:
      if self.max < self.capacity:
        self.max += 1
        return self.max
      else:
        return Null # 크기 초과
    else:
      rec = self.deleted
      self.deleted = self.n[rec].dnext # 프리 리스트에서 다음 삭제된 노드의 인덱스를 가리킨다
      return rec
    
  def delete_index(self, idx: int) -> None:
    """레코드 idx를 프리 리스트에 등록"""
    if self.deleted == Null:
      self.deleted = idx
      self.n[self.deleted].dnext = Null
    else:
      rec = self.deleted
      self.deleted = idx
      self.n[idx].dnext = rec

  def search(self, data: Any) -> int:
    """data와 값이 같은 노드를 검색"""
    cnt = 0
    ptr = self.head
    while ptr != Null:
      if self.n[ptr].data == data:
        self.current = ptr
        return cnt
      cnt += 1
      ptr = self.n[ptr].next
    return Null
  
  def __contains__(self, data: Any) -> bool:
    """연결 리스트에 data가 포함되어 있는지 확인"""
    return self.search(data) > 0
  
  def add_first(self, data: Any):
    ptr = self.head
    rec = self.get_insert_index()
    if rec != Null:
      self.head = self.current = rec
      self.n[self.head] = Node(data, ptr)
      self.no += 1

  def add_last(self, data: Any) -> None:
    if self.head == Null:
      self.add_first(data)
    else:
      ptr = self.head
      while self.n[ptr].next != Null:
        ptr = self.n[ptr].next
      rec = self.get_insert_index()
      if rec != Null:
        self.n[ptr].next = self.current = rec
        self.n[rec] = Node(data)
        self.no += 1

  def remove_first(self) -> None:
    if self.head != Null:
      ptr = self.n[self.head].next
      self.delete_index(self.head)
      self.head = self.current = ptr
      self.no -= 1

  def remove_last(self):
    if self.head != Null:
      if self.n[self.head].next == Null:
        self.remove_first()
      else:
        ptr = self.head # 스캔 중인 노드
        pre = self.head # 스캔 중인 노드의 앞쪽 노드
        while ptr.next != Null:
          pre = ptr
          ptr = self.n[ptr].next
        self.n[pre].next = Null
        self.delete_index(ptr)
        self.current = pre
        self.no -= 1
        
  def remove(self, p: int) -> None:
    if self.head != Null:
      if p == self.head:
        self.remove_first()
      else:
        ptr = self.head
        while self.n[ptr].next != p:
          ptr = self.n[ptr].next
          if ptr == Null:
            return
        self.n[ptr].next == Null
        self.delete_index(ptr)
        self.n[ptr].next = self.n[p].next
        self.current = ptr
        self.no -= 1

  def remove_current_node(self) -> None:
    self.remove(self.current)

  def clear(self) -> None:
    while self.head != Null:
      self.remove_first()
    self.current = Null

  def next(self) -> bool:
    """주목 노드를 한 칸 뒤로 이동"""
    if self.current == Null or self.n[self.current].next == Null:
      return False
    else:
      self.current = self.n[self.current].next
      return True
    
  def print_current_node(self) -> None:
    if self.current == Null:
      print('주목 노드가 존재하지 않습니다.')
    else:
      print(self.n[self.current].data)

  def print(self) -> None:
    ptr = self.head
    while ptr != Null:
      print(self.n[ptr].data)
      ptr = self.n[ptr].next

  def __iter__(self) -> LinkedListIterator:
    """이터레이터를 반환"""
    return LinkedListIterator(self.n, self.head)
  
class LinkedListIterator:
  """클래스 LinkedList의 이터레이터용 클래스"""
  def __init__(self, n: int, head: int):
    self.n = n
    self.current = head
  
  def __iter__(self) -> LinkedListIterator:
    return self
  
  def __next__(self) -> Any:
    if self.current == Null:
      raise StopIteration
    else:
      data = self.n[self.current].data
      self.current = self.n[self.current].next
      return data