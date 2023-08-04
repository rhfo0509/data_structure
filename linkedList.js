class LinkedList {
  length = 0;
  head = null;
  tail = null;

  add(value) {
    // if (this.head) {
    //   let current = this.head;
    //   // linkedList 순회를 while 반복문을 통해 구현
    //   while (current.next) {
    //     current = current.next;
    //   }
    //   current.next = new Node(value);
    //   current.next.prev = current;
    // } else {
    //   this.head = new Node(value);
    // }

    // 삽입의 시간복잡도를 O(1)으로 변경
    if (this.head) {
      let current = this.tail;
      this.tail = new Node(value);
      this.tail.prev = current;
      this.tail.prev.next = this.tail;
    } else {
      this.head = this.tail = new Node(value);
    }
    // 어떤 것을 return하면 좋을지 생각해보면..
    // 이미 인수로 전달된 요소 대신 length 값을 반환하는 것이 더 효율적
    return ++this.length;
  }
  search(index) {
    // let count = 0;
    // let current = this.head;

    // while (count < index) {
    //   current = current?.next;
    //   count++;
    // }
    // return current?.value;
    return this.#search(index)[1]?.value;
  }
  #search(index) {
    let count = 0;
    let prev;
    let current = this.head;

    while (count < index) {
      prev = current;
      current = current?.next;
      count++;
    }
    return [prev, current];
  }
  remove(index) {
    const [prev, current] = this.#search(index);
    if (prev && current) {
      prev.next = current.next;
      return --this.length;
    } else if (current) {
      // index가 0일 때의 처리를 여기서 작성
      this.head = current.next;
      return --this.length;
    }
    // 삭제하고자 하는 대상이 없는 경우 아무 것도 하지 않는다.
  }
}

class Node {
  next = null;
  prev = null;
  constructor(value) {
    this.value = value;
  }
}

const li = new LinkedList();

li.add(1);
li.add(2);
li.add(3);
li.add(4);
li.add(5);
li.add(6);

console.log(li.search(2));
console.log(li.search(4));
console.log(li.search(6));

li.remove(4);
li.remove(4);
li.remove(4);
