export class BinarySearchTree {
  root = null;
  length = 0;

  #insert(node, value) {
    if (node.value > value) {
      if (!node.left) {
        node.left = new Node(value);
      } else {
        // 루트노드보다 작은 값이면 left subtree에게 값 판단을 위임
        this.#insert(node.left, value);
      }
    } else if (node.value < value) {
      if (!node.right) {
        node.right = new Node(value);
      } else {
        // 루트노드보다 큰 값이면 right subtree에게 값 판단을 위임
        this.#insert(node.right, value);
      }
    } else {
      throw new Error("값이 이미 존재합니다.");
    }
  }
  insert(value) {
    // 어떤 값을 넣을 때 우선 왼팔, 오른팔에게 맡기고
    // 왼팔이나 오른팔이 존재하지 않으면 거기에다가 값을 넣는다.
    if (!this.root) {
      this.root = new Node(value);
    } else {
      this.#insert(this.root, value);
    }
    return ++this.length;
  }
  #search(node, value) {
    if (node.value > value) {
      if (!node.left) {
        return null;
      }
      if (node.left.value === value) {
        return node.left;
      }
      return this.#search(node.left, value);
    } else {
      if (!node.right) {
        return null;
      }
      if (node.right.value === value) {
        return node.right;
      }
      return this.#search(node.right, value);
    }
  }
  search(value) {
    if (!this.root) {
      return null;
    }
    if (this.root.value === value) {
      return this.root;
    }
    return this.#search(this.root, value);
  }
  #remove(node, value) {
    // 제거할 값이 BST에 존재하지 않는 경우
    if (!node) {
      return null;
    }
    // 값을 찾은 경우 (자식 노드에서 수행됨)
    if (node.value === value) {
      this.length--;
      // 1번의 경우
      if (!node.left && !node.right) {
        return null;
      } 
      // 2번의 경우
      else if (!node.left) {
        return node.right;
      } 
      // 3번의 경우
      else if (!node.right) {
        return node.left;
      } 
      // 4번의 경우
      else {
        // exchange: 찾은 노드 기준 좌측에서 "가장 우측"에 위치한 노드 -> leaf
        let exchange = node.left;
        while (exchange.right) {
          exchange = exchange.right;
        }
        let temp = node.value;
        node.value = exchange.value;
        exchange.value = temp;
        // 교체 이후 leaf가 된 찾은 노드를 제거
        // node.value === value가 되는 상황이 한번 더 발생하므로 미리 length를 증가시킴
        this.length++;  
        node.left = this.#remove(node.left, exchange.value);
        return node;
      }
    }
    // 값을 찾지 못한 경우 (부모 노드에서 수행됨)
    // 자식으로부터 값을 전달받는다.
    else {
      if (node.value > value) {
        node.left = this.#remove(node.left, value);
        return node;
      } else {
        node.right = this.#remove(node.right, value);
        return node;
      }
    }
  }
  remove(value) {
    // 1. leaf(양팔 다 없음) => 제거
    // 2. leaf X, 왼팔이 없음 => 오른팔 끌어올린다.
    // 3. leaf X, 오른팔이 없음 => 왼팔 끌어올린다.
    // 4. leaf X, 양팔 존재 => 왼팔에서 가장 큰 노드와 자리 체인지 후 leaf를 지운다.

    this.root = this.#remove(this.root, value);
    return this.length; // length를 return하도록 (숙제)
  }
}
class Node {
  left = null;
  right = null;
  constructor(value) {
    this.value = value;
  }
}

// const bst = new BinarySearchTree();

// bst.insert(8);
// bst.insert(10);
// bst.insert(3);
// bst.insert(1);
// bst.insert(14);
// bst.insert(6);
// bst.insert(7);
// bst.insert(4);
// bst.insert(13);
// console.log(bst.search(7));
// console.log(bst.search(5));
// bst.remove(8);
// console.log(bst.remove(15));
// bst.remove(4);

// const bst2 = new BinarySearchTree();

// bst2.insert(50);
// bst2.remove(50);
// console.log(bst2.root);


