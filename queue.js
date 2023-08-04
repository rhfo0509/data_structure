export class Queue {
  arr = [];

  enqueue(value) {
    return this.arr.push(value);
  }
  dequeue() {
    return this.arr.shift();
  }
  peek() {
    return this.arr.at(0);
  }
  get length() {
    return this.arr.length;
  }
}

// const queue = new Queue();

// queue.enqueue(2); // 1
// queue.enqueue(4); // 2
// queue.enqueue(1); // 3
// queue.enqueue(3); // 4
// queue.enqueue(5); // 5

// queue.dequeue();   // 2
// console.log(queue.peek());   // 4
// console.log(queue.length);  // 4