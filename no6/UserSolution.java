class Node {
  public int data;
  public Node next;

  public Node(int data) {
    this.data = data;
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
  }

  public void addNode2Head(int data) {
    Node currNode = getNode(data);
    if (head.next != null) {
      currNode.next = this.head.next;
      this.head.next = currNode;
      return;
    }
    this.head.next = currNode;
  }

  public void addNode2Tail(int data) {
    if (this.head.next == null) {
      this.head.next = getNode(data);
      return;
    }
    Node currNode = this.head.next;
    while (currNode.next != null) {
      currNode = currNode.next;
    }
    currNode.next = getNode(data);
  }

  public void addNode2Num(int data, int num) {
    Node currNode = this.head.next;
    Node prevNode = this.head;
    Node newNode = getNode(data);
    for (int i = 1; i < num; i++) {
      prevNode = currNode;
      currNode = currNode.next;
    }
    prevNode.next = newNode;
    newNode.next = currNode;
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
}