# https://www.youtube.com/watch?v=S6IfqDXWa10&t=19s

# we will use hash map and doubly linked list here
# deletion in doubly linked list takes O(1) time 
# where as insertion and deletion in hash map also takes O(1) time
# but we uses doubly linked to implement LRU 

# put()
# if key not in hash map then:
# create node, and insert in the double linked list
# then insert it in hash map
# if already in the hash map then:
# remove the node from its doubly linked list position
# put it into the head of the doubly linked list with updated value
# update the node and value in the hash map

# get()
# go to the hash map, if not present then return -1
# if present got to the node and return its value
# remove the node from its doubly linked list position
# put it into the head of the doubly linked list with updated value

# if length exceeds the max length(no of slots = 5 )
# remove the last node from the doubly linked list

from typing import Dict

class Node:
	def __init__(self,key=None,val=None,next=None,prev=None):
		self.key = key
		self.val = val
		self.next = next
		self.prev = prev
	def __str__(self):
		return f"{self.key} -> {self.val} ;"
class DoublyLinkedList:
	def __init__(self):
		self.max_length=5
		self.current_length=0
		self.head =  Node()
		self.tail = Node()

		self.head.next = self.tail
		self.tail.prev=self.head

		self.node_ref = {}

	def insert_in_list(self,current):
		temp =self.head.next
		current.next=temp
		current.prev=self.head 
		self.head.next=current
		temp.prev=current
		
		self.current_length +=1

		if self.current_length > self.max_length:
			self.remove_from_list(self.tail.prev)
	def remove_from_list(self,current):
		prev_node = current.prev
		next_node = current.next
		prev_node.next=next_node
		next_node.prev=prev_node
		self.current_length -=1

	def put(self,key,val):
		if key not in self.node_ref:
			current = Node(key,val)
			self.insert_in_list(current)
			self.node_ref[key]=current
		else:
			current = self.node_ref[key]
			current.val = val
			self.remove_from_list(current)
			self.insert_in_list(current)

	def get(self,key):
		if key not in self.node_ref:
			return -1
		current = self.node_ref[key]
		val= current.val
		self.remove_from_list(current)
		self.insert_in_list(current)
		return val

	def show_list(self):
		current = self.head.next
		while current!=self.tail:
			print(current)
			current = current.next
		print("-------------------------------")

if __name__ == '__main__':
	cache=DoublyLinkedList()
	cache.put(1,1)
	cache.put(2,3)
	cache.show_list()
	# 2 -> 3 ;
	# 1 -> 1 ;
	cache.put(3,4)
	cache.put(6,10)
	cache.show_list()
	# 6 -> 10 ;
	# 3 -> 4 ;
	# 2 -> 3 ;
	# 1 -> 1 ;
	cache.put(7,13)
	cache.put(1,25)
	cache.put(9,10)
	cache.show_list()
	# 9 -> 10 ;
	# 1 -> 25 ;
	# 7 -> 13 ;
	# 6 -> 10 ;
	# 3 -> 4 ;
	print(cache.get(1))
	print(cache.get(90))
	cache.show_list()
	# 25
	# -1
	# 1 -> 25 ;
	# 9 -> 10 ;
	# 7 -> 13 ;
	# 6 -> 10 ;
	# 3 -> 4 ;
