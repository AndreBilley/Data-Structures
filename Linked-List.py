class Linked_List:
    def __init__(self):
        self.start_node = None

    def traverse(self):
        # check if LL is empty
        # check if self.start_node is None
        if self.start_node == None:
            print ("List is empty")
        else:
            node = self.start_node
            while node:
                print(node.data)
                node = node.next_node

        # Node must be an instance of node
        # If the LL is not empty then
        # self.start_node will be an instance of Node

    def add_node(self, new_node):
        # Add to beginning
        # 1. List is empty
        # 2. new_node is smaller than the first node
        if self.start_node == None:
            self.start_node = new_node
        else:
            node = self.start_node
            previous = None
        # Add to middle
            while node:
                if ord(node.data) > ord(new_node.data):
                    new_node.next_node = node
                    if previous == None:
                        self.start_node = new_node
                        return
                    else:
                        previous.next_node = new_node
                        return
                previous = node
                node = node.next_node
        # Add to end
            previous.next_node = new_node
        pass

    def remove_node(self, node_to_remove):
        # Remove from beginning
        # Remove from middle
        # Remove from end
        if not self.start_node: # If empty
            print("List is empty")
        else:
            node = self.start_node
            previous = None
            while node:
                if node.data == node_to_remove:  
                    if previous:
                        previous.next_node = node.next_node    
                    else:
                        self.start_node = node.next_node
                previous = node
                node = node.next_node
        pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

# Initilising LinkedList
linked_list = Linked_List()


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
        linked_list.add_node(Node(item))
        linked_list.traverse()
    if opt == '2':
        item = input('Enter item: ')
        linked_list.remove_node(item)
        linked_list.traverse()
    if opt == '3':
        linked_list.traverse()
    if opt == '4':
        run = False