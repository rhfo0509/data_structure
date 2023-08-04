class PriorityQueue {
  arr = [];

  #reheapUp(index) {
    if (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);
      if (this.arr[index].priority > this.arr[parentIndex].priority) {
        let temp = this.arr[parentIndex];
        this.arr[parentIndex] = this.arr[index];
        this.arr[index] = temp;
        // 이제 부모로 끌어올려진 요소에 대해 재귀 수행
        this.#reheapUp(parentIndex);
      }
    }
  }
  insert(priority, value) {
    const index = this.arr.length;
    this.arr[index] = {
      priority,
      value,
    };
    // 부모랑 비교하면서 부모보다 값이 더 크면 요소를 끌어올리는 과정
    this.#reheapUp(index);
  }
  #reheapDown(index) {
    const leftIndex = index * 2 + 1;
    if (leftIndex < this.arr.length) {
      const rightIndex = index * 2 + 2;
      const bigger =
        this.arr[leftIndex].priority > (this.arr[rightIndex]?.priority || 0) ? leftIndex : rightIndex;
      if (this.arr[index].priority < this.arr[bigger]?.priority) {
        let temp = this.arr[bigger];
        this.arr[bigger] = this.arr[index];
        this.arr[index] = temp;
        this.#reheapDown(bigger);
      }
    }
  }
  remove() {
    if (!this.arr.length) {
      return false;
    }
    if (this.arr.length === 1) {
      // 루트 노드만 존재하는 경우 pop만 하면됨. (reheapDown을 수행하지 않음)
      return this.arr.pop();
    }
    const root = this.arr[0];
    this.arr[0] = this.arr.pop();
    this.#reheapDown(0);
    return root;
  }
  sort() {
    const sortedArray = [];
    while (this.arr.length) {
      // 데이터가 내림차순으로 정렬됨 (가장 큰 값인 루트 노드를 제거하므로)
      sortedArray.push(this.remove());
    }
    return sortedArray;
  }
  search(value) {
    for (let i = 0; i < this.arr.length; i++) {
      if (this.arr[i].value === value) {
        return i;
      }
    }
    return null;
  }
  update(value, newValue) {
    const index = this.search(value);
    if (index === null) {
      return false;
    }
    this.arr[index].value = newValue;
    // 마지막부터 세었을 때 leaf가 아닌 첫번째 노드부터 루트 노드까지 heapify 수행
    // 이 반복 횟수가 O(n)에 해당하고 실제 heapify 내부 로직은 O(1)에 해당한다.
    for (let i = Math.floor(this.arr.length / 2 - 1); i >= 0; i++) {
      this.#heapify(i);
    }
  }
  // "특정" 값 삭제
  removeValue(value) {
    const index = this.search(value);
    if (index === null) {
      return false;
    }
    this.arr.splice(index, 1);
    for (let i = Math.floor(this.arr.length / 2 - 1); i >= 0; i++) {
      this.#heapify(i);
    }
  }
  // "특정" 값을 수정하거나 삭제할 때 내부적으로 수행되는 알고리즘
  #heapify(index) {
    const leftIndex = index * 2 + 1;
    const rightIndex = index * 2 + 2;
    // undefined가 비교되는 것을 방지
    const bigger =
      (this.arr[leftIndex]?.priority || 0) > (this.arr[rightIndex]?.priority || 0)
        ? leftIndex
        : rightIndex;
    if (this.arr[index].priority < (this.arr[bigger]?.priority || 0)) {
      let temp = this.arr[bigger];
      this.arr[bigger] = this.arr[index];
      this.arr[index] = temp;
      this.#reheapDown(bigger);
    }
  }
}

const pq = new PriorityQueue();
pq.insert(3, "one");
pq.insert(7, "two");
pq.insert(2, "three");
pq.insert(8, "four");
pq.insert(5, "five");
pq.insert(6, "six");
pq.insert(9, "king");
console.log(pq.remove()); // 'king'
pq;