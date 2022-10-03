### testing python3 linked list implementation
from Node import Node

class LinkedList:
   def __init__(self):
      self.head_node = None
   
   def insert_at_head(self, data):
      temp_node = Node(data)
      temp_node.next_element = self.head_node
      self.head_node = temp_node
      return self.head_node

   def is_empty(self):
      if self.head_node is None:
          return True
      else:
          return False

   def print_list(self):
      if (self.is_empty()):
          print("List is Empty")
          return False
      temp = self.head_node
      while temp.next_element is not None:
          print(temp.data, end=" -> ")
          temp = temp.next_element
      print(temp.data, "-> None")
      return True

list = LinkedList()
list.print_list()

print("Inserting values in list")
for i in range(1, 10):
    list.insert_at_head(i)
list.print_list()
   
