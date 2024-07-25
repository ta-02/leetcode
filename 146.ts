type cacheNode = {
  value: number;
  next?: cacheNode;
  prev?: cacheNode;
};

const createNode = (value: number): cacheNode => ({ value });

class LRUCache {
  private capacity: number;
  private length: number;
  private head?: cacheNode;
  private tail?: cacheNode;
  private lookup: Map<number, cacheNode>;
  private reverseLookup: Map<cacheNode, number>;

  constructor(capacity: number) {
    this.capacity = capacity;
    this.length = 0;
    this.head = this.tail = undefined;
    this.lookup = new Map<number, cacheNode>();
    this.reverseLookup = new Map<cacheNode, number>();
  }

  get(key: number): number {
    const ListNode = this.lookup.get(key);
    if (!ListNode) {
      return -1;
    }
    this.detach(ListNode);
    this.prepend(ListNode);
    return ListNode.value;
  }

  put(key: number, value: number): void {
    const ListNode = this.lookup.get(key);
    if (ListNode) {
      ListNode.value = value;
      this.detach(ListNode);
      this.prepend(ListNode);
      return;
    }
    const newNode = createNode(value);
    this.length++;
    this.prepend(newNode);
    this.evict();
    this.lookup.set(key, newNode);
    this.reverseLookup.set(newNode, key);
  }

  private detach(node: cacheNode) {
    if (node.prev) {
      node.prev.next = node.next;
    }
    if (node.next) {
      node.next.prev = node.prev;
    }
    if (this.head === node) {
      this.head = this.head.next;
    }
    if (this.tail === node) {
      this.tail = this.tail.prev;
    }
    node.prev = undefined;
    node.next = undefined;
  }

  private prepend(node: cacheNode) {
    if (!this.head) {
      this.head = this.tail = node;
    } else {
      node.next = this.head;
      this.head.prev = node;
      this.head = node;
    }
  }

  private evict() {
    if (this.length <= this.capacity) {
      return;
    }
    const tail = this.tail as cacheNode;
    this.detach(tail);
    const key = this.reverseLookup.get(tail) as number;
    this.lookup.delete(key);
    this.reverseLookup.delete(tail);
    this.length--;
  }
}
