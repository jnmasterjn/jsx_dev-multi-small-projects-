#this is a python class that builds our own double linked list
# None <- node1 -> <- node2 -> <- node3 -> <- None (double linked list)

class Node:
    def __init__(self, data):
        self.item=data
        self.next=None
        self.prev=None

class Double_linked_list:
    def __init__(self):
        self.start_node=None
        
    def insert_from_back(self,data):
        if self.start_node==None:
            new_node=Node(data)
            self.start_node=new_node

        else:
            current_node=self.start_node

            while current_node.next is not None: 
                current_node=current_node.next
        
            new_node=Node(data)
            new_node.prev=current_node
            current_node.next=new_node

    def display_list(self):
        if self.start_node==None:
            print("Empty List")
        
        else:
            index=0 
            current_node=self.start_node
            
            while current_node.next is not None:

                print(index, ":", current_node.item, type(current_node.item))

                current_node=current_node.next
                index=index+1

            print(index, ":", current_node.item, type(current_node.item))


    def delete_from_end(self):
        if self.start_node==None:
            return 
        
        if self.start_node==None:
            self.start_node= None
            return
        
        current_node=self.start_node
        while current_node.next is not None:
            current_node= current_node.next

        current_node.prev.next==None    
        



my_list=Double_linked_list()
my_list.insert_from_back("A")
my_list.insert_from_back("B")
my_list.insert_from_back("C")
my_list.insert_from_back("D")
my_list.insert_from_back("E")

my_list.display_list()

print("----------------------")
print("Delete from end: ")
my_list.delete_from_end()
my_list.display_list()





print("======================")
print(my_list.start_node.item)
print("hi" + my_list.start_node.next.item)     



    
