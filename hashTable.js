class HashTable {
  // 공간복잡도: O(n)
  data = [];
  constructor(capa) {
    // 해시 테이블의 용량
    this.capa = capa; 
  }
  // insert 시간복잡도: O(1)
  insert(key, value) {
    const hash = hashF(key, this.capa);
    if (!this.data[hash]) {
      this.data[hash] = [];
    }
    this.data[hash].push({ key, value });
  }
  // search 시간복잡도: O(n/hash)
  // 해시함수의 성능에 따라 hash가 1이 되어 O(n)이 될 수도, hash가 n이 되어 O(1)이 될 수도 있다.
  search(key) {
    const hash = hashF(key, this.capa);
    if (this.data[hash]) {
      for (let i = 0; i < this.data[hash].length; i++) {
        if (this.data[hash][i].key === key) {
          return this.data[hash][i].value;
        }
      }
    }
    return null;
  }
  // update 시간복잡도: O(n/hash)
  update(key, value) {
    const hash = hashF(key, this.capa);
    if (this.data[hash]) {
      for (let i = 0; i < this.data[hash].length; i++) {
        if (this.data[hash][i].key === key) {
          this.data[hash][i].value = value;
        }
      }
    }
  }
  // delete 시간복잡도: O(n/hash)
  delete(key) {
    const hash = hashF(key, this.capa);
    if (this.data[hash]) {
      for (let i = 0; i < this.data[hash].length; i++) {
        if (this.data[hash][i].key === key) {
          this.data[hash].splice(i, 1);
        }
      }
    }
  }
}
function hashF(key, mod) {
  // mod에는 해시테이블의 용량(capa)이 들어감
  if (typeof key === 'number') {
    return key % mod;
  }
  if (typeof key === 'string') {
    return key.split('').reduce((a, c) => a + c.charCodeAt(), 0) % mod
    // 'abc' -> ['a', 'b', 'c'] -> [97, 98, 99] -> 294 % 30 = 24
  }
}

const ht = new HashTable(30);
ht.insert('abc', 'hi');
ht.insert(31, 'hello');
ht.insert(61, 'bye');
ht.insert(83, true);
ht.insert(115, 135);
console.log(ht.search(61));
console.log(ht.search(99));
ht.update(83, false);
ht.delete(31);
ht;