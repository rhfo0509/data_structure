from __future__ import annotations
from typing import Any, Type

class Node:
  """이진 검색 트리의 노드"""
  def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
    self.key = key
    self.value = value
    self.left = left
    self.right = right

class BinarySearchTree:
  """이진 검색 트리"""
  def __init__(self):
    self.root = None

  def search(self, key: Any) -> Any:
    """키가 key인 노드를 검색"""
    p = self.root
    while True:
      if p is None:
        return None
      if key == p.key:
        return p.value
      elif key < p.key:
        p = p.left
      else:
        p = p.right

  def add(self, key: Any, value: Any) -> bool:
    """키가 key이고 값이 value인 노드를 삽입"""
    def add_node(node: Node, key: Any, value: Any) -> None:
      """node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입"""
      if key == node.key:
        return False
      elif key < node.key:
        if node.left is None:
          node.left = Node(key, value, None, None)
        else:
          add_node(node.left, key, value)
      else:
        if node.right is None:
          node.right = Node(key, value, None, None)
        else:
          add_node(node.right, key, value)
      return True

    if self.root is None:
      self.root = Node(key, value, None, None)
      return True
    else:
      return add_node(self.root, key, value)
    
  def remove(self, key: Any) -> bool:
    """키가 key인 노드를 삭제"""
    p = self.root               # 스캔 중인 노드
    parent = None               # 스캔 중인 노드의 부모 노드
    is_left_child = True        # p는 parent의 왼쪽 자식 노드인지 확인

    while True:
      if p is None:
        return False
      
      if key == p.key:
        break
      else:
        parent = p              # 가지를 내려가기 전에 부모를 설정
        if key < p.key:
          is_left_child = True
          p = p.left
        else:
          is_left_child = False
          p = p.right

    # 1,2번 case: 자식 노드가 없는 노드를 삭제하는 경우 + 자식 노드가 1개인 노드를 삭제하는 경우 
    if p.left is None:          # p에 왼쪽 자식이 없으면
      if p is self.root:
        self.root = p.right
      elif is_left_child:
        parent.left = p.right   # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
      else:
        parent.right = p.right  # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
    elif p.right is None:       # p에 오른쪽 자식이 없으면
      if p is self.root:
        self.root = p.left
      elif is_left_child:
        parent.left = p.left    # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
      else:
        parent.right = p.left   # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴
    # 3번 case: 자식 노드가 2개인 노드를 삭제하는 경우
    else:
      parent = p
      left = p.left             # 서브트리 안에서 가장 큰 노드
      is_left_child = True
      # left에서 오른쪽 끝까지 이동하면서 가장 큰 노드를 찾음 
      while left.right is not None:
        parent = left
        left = left.right
        is_left_child = False
      p.key = left.key          # left의 키를 p로 이동
      p.value = left.value      # left의 데이터를 p로 이동
      # left의 키와 데이터를 복사했으면 기존의 left 노드는 제거해야 함함
      if is_left_child:
        parent.left = left.left
      else:
        parent.right = left.left
    return True