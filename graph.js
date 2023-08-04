class Graph {
  vertices = [];
  matrix = [];

  insertVertex(name) {
    this.vertices.push(new Vertex(name));
    // vertex 추가할 때마다 빈 2차원 배열을 insert
    this.matrix.push([]);
  }
  #searchVertex(name) {
    for (let i = 0; i < this.vertices.length; i++) {
      if (this.vertices[i].name === name) {
        return i;
      }
    }
    return null;
  }
  insertArc(from, to, value, capacity) {
    const fromV = this.#searchVertex(from);
    const toV = this.#searchVertex(to);
    if (fromV === null || toV === null) {
      throw new Error("찾는 버텍스가 없습니다.");
    }
    this.matrix[fromV][toV] = new Arc(value, capacity);
  }
}

class Vertex {
  constructor(name) {
    this.name = name;
  }
}

class Arc {
  constructor(value, capacity) {
    // 실제 값은 value에, 수용량은 capacity에 저장
    this.value = value;
    this.capacity = capacity;
  }
}

const g = new Graph();
g.insertVertex('a');
g.insertVertex('b');
g.insertVertex('c');
g.insertArc('a', 'b', 3);
// arc는 양방향일 때 서로 다른 value(, capa)를 가질 수 있음
g.insertArc('a', 'c', 2);
g.insertArc('c', 'a', 4);
g.insertArc('b', 'c', 1);
g;