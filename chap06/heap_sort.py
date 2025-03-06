from typing import MutableSequence

def heapify(a: MutableSequence, n: int, i: int) -> None:
    """
    힙 속성을 유지하도록 배열을 재구성하는 함수
    - a: 정렬할 리스트
    - n: 리스트의 크기
    - i: 부모 노드의 인덱스
    """
    largest = i  # 부모 노드
    left = 2 * i + 1  # 왼쪽 자식 노드
    right = 2 * i + 2  # 오른쪽 자식 노드
    
    # 왼쪽 자식 노드가 부모보다 크다면 교체
    if left < n and a[left] > a[largest]:
        largest = left
    
    # 오른쪽 자식 노드가 부모보다 크다면 교체
    if right < n and a[right] > a[largest]:
        largest = right
    
    # 바뀐 자식 노드 위치에서 다시 힙 속성을 확인한다 (재귀 호출)
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heap_sort(a: MutableSequence) -> None:
    """
    힙 정렬을 수행하는 함수
    - a: 정렬할 리스트
    """
    n = len(a)
    
    # 최대 힙 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    
    # 정렬 과정 (힙에서 요소 하나씩 제거)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]  # 최댓값(루트)을 리스트의 끝으로 이동
        heapify(a, i, 0)  # 줄어든 크기에 대해 다시 힙 정렬