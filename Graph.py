class Queue():
    def __init__(self, max_size):
        self.head = None
        self.end = None
        self.max_size = max_size
        self.current_num = 0

    def enQueue(self, node, priority=False):
        # 3 cases
        # When the queue is full
        if self.isFull():
            print('Cannot add to full queue')

        # When queue is empty
        if self.isEmpty():
            self.head = node
            self.end = node
            self.current_num += 1
            print('Added successfully')

        else:
            self.end.next_node = node
            self.end = node
            print('Added successfully')
            

    def deQueue(self, node):
        if self.isEmpty():
            print('Cannot remove from empty queue')

        else: 
            first = self.head
            self.head = self.head.next_node
            self.current_num -= 1
            print('Removed successfully')
            return first
            
    def isEmpty(self):
        return self.current_num == 0

    def isFull(self):
        return self.max_size == self.current_num

    def traverse(self):
        node = self.head
        print('Current Graph')
        while node:
            print(node.data)
            node = node.next_node


class Node():
    def __init__(self, data):
        self.data = data
        self.next_node = None

q = Queue(10)
print('Queue')


# User Interface
run = True
while run:
    opt = input('''
1. Add an item
2. Remove an item
3. Traverse
4. Exit
> ''')
    if opt == '1':
        item = input('Enter item: ')
        q.enQueue(Node(item))
    if opt == '2':
        item = input('Enter item: ')
        q.deQueue(Node(item))
    if opt == '3':
        q.traverse()
    if opt == '4':
        run = False