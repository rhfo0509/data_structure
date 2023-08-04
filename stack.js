export class Stack {
  arr = [];

  push(value) {
    return this.arr.push(value);
  }
  pop() {
    return this.arr.pop();
  }
  top() {
    return this.arr.at(-1);
  }
  get length() {
    return this.arr.length;
  }
}

// const stack = new Stack();

// stack.push(2); // 1
// stack.push(4); // 2
// stack.push(1); // 3
// stack.push(3); // 4
// stack.push(5); // 5

// stack.pop();   // 5
// console.log(stack.top());   // 3
// console.log(stack.length);  // 4