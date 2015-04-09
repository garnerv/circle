#  File: Josephus.py

#  Description: Program to solve the Josephus problem using a circular linked list.

#  Student Name: Garner Vincent

#  Student UT EID: GV4353

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 3-31-15

#  Date Last Modified: 4-4-15

class Link(object):
	#constructor with default none val
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

class CircularList(object):
	#constructor with default first as none
	def __init__ (self):
		self.first = None

	#inserts a link and connects it to the first link
	def insert (self, item):
		newLink = Link(item)

		if self.first == None:
			self.first = newLink
			newLink.next = self.first
			self.first = newLink
			return
		#start the traversal at the first link
		current = self.first

		#traverse the circular list until the link before the first is found
		while current.next != self.first:
			current = current.next

		#assign the new link to the current.next value
		current.next = newLink
		#link new link to the first link
		newLink.next = self.first
		#link the current and previous link
		newLink.previous = current
	
	#function to return none if the key is not in the list, and returns the link if found
	def find (self, key):
		#check if the list is empty
		if self.first == None:
			return None
		#assign the traversal starting point as the first link
		current = self.first
		#traverse the list until key is found, return none if not found
		while (current.data != key):
			if current.next == self.first:
				return None
			else:
				current = current.next

		#return current link if found
		return current

	#fucntion that will retun the length of a given list
	def __len__ (self):
		if self.first == None:
			return 0

		count = 1
		current = self.first
		while current.next != self.first:
			count += 1
			current = current.next
		return count

	#function to delete a link from the list
	def delete (self, key):
		#return none if the list is empty
		if self.first == None:
			return None

		#track the current and previous links during traversal
		current = self.first
		previous = self.first

		#make the first previous link the one before the first in a list len > 1
		while previous.next != self.first:
			previous = previous.next

		#loop through the list until the key is found
		while current.data != key:
			#return none if the key is not found and the next element is the first element
			if current.next == self.first:
				return None
			#assign new previous and current if key not found
			previous = current
			current = current.next

		#if the link to delete is the first link, assign the new first link as the next link
		if current == self.first:
			if self.first == self.first.next:
				self.first = None
				return current
			else:
				self.first = current.next

		#assign new linked values

		previous.next = current.next

		#return the 
		return current

	def deleteAfter (self, start, n):
		if self.first == None:
			return None
		#initialize start link for traversal, traverse list until the start link for this elimination round is found
		current = self.first
		while (current.data != start):
			current = current.next
		#traverse until the nth link
		count = 1
		while (count != n):
			current = current.next
			count += 1
		#delete the link with the data value present in the current link 
		self.delete(current.data)

		#print out the data in the link deleted to the console
		print(current.data, end = " ")
		#return the next data value to the function
		return current.next

	def __str__(self):
		#if the list is empty, return none
		if self.first == None:
			return "None"
		#else, format the list as a normal looking python list
		else:
			lst = "["
			current = self.first
			while current.next != self.first:
				lst += str(current.data) + ", "
				current = current.next
			lst += str(current.data) + "]"
			return lst

def main():
	#read in josephus text file, assign data points
	inFile = open("./Josephus.txt", "r")
	numSoldiers = int(inFile.readline().strip())
	startCount = int(inFile.readline().strip())
	elimNum = int(inFile.readline().strip())
	#close file, done reading
	inFile.close()
	#create circular list
	a = CircularList()

	#create a sequential list of the number of soldiers specified
	for i in range(1, numSoldiers + 1):
		a.insert(i)


	#delete the soldiers using the deleteAfter function
	for i in range(numSoldiers):
		#delete the item, set start count equal to the memory address of the next link
		startCount = a.deleteAfter(startCount, elimNum)
		#pull the data from this memory address for the next iteration
		startCount = startCount.data
	#print a line so the formatting looks good
	print()


main()

