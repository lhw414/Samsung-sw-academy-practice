class Node {
  public int data;
  public Node prev;
  public Node next;

  public Node(int data) {
    this.data = data;
    this.prev = null;
    this.next = null;
  }
}

public class UserSolution {

  private final static int MAX_NODE = 10000;

  private Node[] node = new Node[MAX_NODE];
  private int nodeCnt = 0;
  private Node head;

  public Node getNode(int data) {
    node[nodeCnt] = new Node(data);
    return node[nodeCnt++];
  }

  public void init() {
    head = new Node(99);
    head.next = null;
    head.prev = null;
  }

  public void addNode2Head(int data) {
    Node currNode = getNode(data);
    if (head.next != null) {
      currNode.next = head.next;
      currNode.next.prev = currNode;
      this.head.next = currNode;
      currNode.prev = this.head;
      return;

    }
    this.head.next = currNode;
    currNode.prev = this.head;
  }

  public void addNode2Tail(int data) {
    if (this.head.next == null) {
      Node newNode = getNode(data);
      this.head.next = newNode;
      newNode.prev = this.head;
      return;
    }
    Node currNode = this.head.next;
    while (currNode.next != null) {
      currNode = currNode.next;
    }
    Node newNode = getNode(data);
    currNode.next = newNode;
    newNode.prev = currNode;
  }

  public void addNode2Num(int data, int num) {
    Node currNode = this.head.next;
    Node prevNode = this.head;
    Node newNode = getNode(data);
    for (int i = 1; i < num; i++) {
      prevNode = currNode;
      currNode = currNode.next;
      if (currNode == null) {
        prevNode.next = newNode;
        newNode.prev = prevNode;
        return;
      }
    }
    prevNode.next = newNode;
    newNode.prev = prevNode;
    newNode.next = currNode;
    currNode.prev = newNode;
  }

  public int findNode(int data) {
    int i = 1;
    Node currNode = this.head.next;
    Node prevNode = this.head;
    while (currNode != null) {
      if (currNode.data == data) {
        break;
      }
      prevNode = currNode;
      currNode = currNode.next;
      i++;
    }
    return i;
  }

  public void removeNode(int data) {
    Node currNode = this.head.next;
    Node prevNode = this.head;
    while (currNode != null) {
      if (currNode.data == data) {
        prevNode.next = currNode.next;
      }
      prevNode = currNode;
      currNode = currNode.next;
    }
  }

  public int getList(int[] output) {
    int cnt = 0;
    int i = 0;
    Node currNode = this.head.next;
    while (currNode != null) {
      cnt++;
      output[i] = currNode.data;
      i++;
      currNode = currNode.next;
    }
    return cnt;
  }


  public int getReversedList(int[] output) {
    int cnt = 0;
    Node currNode = this.head.next;
    while (currNode.next != null) {
      cnt++;
      currNode = currNode.next;
    }
    cnt++;
    for (int i = 0; i < cnt; i++) {
      output[i] = currNode.data;
      currNode = currNode.prev;
    }
    return cnt;
  }
}