# ------------------TASK 1-------------------------------
# Define a class called Stack to implement a stack data structure
class Stack:

 # Initialize the stack with an empty list to store items
    def __init__(self):
        self.items = []

 # Get the number of items in the stack
    def size(self):
        return len(self.items)

 # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

 # Push an item onto the stack
    def push(self,item):
        self.items.append(item)

 # Pop (remove and return) an item from the stack if the stack is not empty
    def pop(self) :
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Cannot pop from an empty stack."
 # Peek at the top item of the stack without removing it, if the stack is not empty
    def peek(self) :
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Empty stack."

#---------------------TASK 2----------------------------
 # Function to reverse a string using a stack
    def reverse_string(self,input_str):
        # Push each character of the input string onto the stack
        for char in input_str:
            self.push(char)

        reversed_str = ""
        # Pop each character from the stack to construct the reversed string
        while not self.is_empty():
            reversed_str += self.pop()
        return reversed_str

#---------------------TASK 3----------------------------
# write a function in the TextEditor class to simulate the "undo" operation
class TextEditor:
# Initialize the text editor with an empty document and an empty undo stack
    def __init__(self):
        self.document =""
        # Create an instance of the Stack class to use as the undo stack
        self.undo_stack =Stack()

# Method to make changes to the document   
    def make_change(self,change):
        self.undo_stack.push(self.document)
        # Apply the change to the document
        self.document += change

# Method to perform undo operation
    def undo(self):
        if not self.undo_stack.is_empty():
            # Revert the document to its previous state by popping from the undo stack
            self.document = self.undo_stack.pop()
        else:
            print("nothing to undo.")
            
# Method to get the current document state
    def get_document(self):
        # Method to get the current document state
        return self.document





#-------------test outputs of task1------------
# Example usage
# Create an instance of the Stack class
stack = Stack()

# Push items onto the stack
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)

# Print the size of the stack and the top element
print("Stack size:", stack.size())
print("Top element:", stack.peek())

# Pop an item from the stack, and print the popped item, and the updated size and top element
popped_item = stack.pop()
print("\nPopped item:", popped_item)
print("\nStack size:", stack.size())
print("Top element:", stack.peek())


#----------------------------------------
# Create another instance of the Stack class
stack1 = Stack()

# Print the size of the empty stack and attempt to pop an item (with an error message)
print("\nStack1 size:", stack1.size())
popped_item = stack1.pop()
print("\nPopped item:", popped_item) 


#-------------test outputs of task2------------
# List of input strings
input_strings = ["hello", "python", "ninebit", "pragati"]

 # Create an instance of the Stack class
stack = Stack()

# Iterate over each string in the list and print the original and reversed strings
for string in input_strings:
    reversed_str = stack.reverse_string(string)
    print("Original String:", string,"||","Reversed String:", reversed_str)
    



#-------------test outputs of task3------------
# Example usage:
text_editor = TextEditor()

# Make changes to the document
text_editor.make_change("Hello ")
text_editor.make_change("world! ")

print("Current document:", text_editor.get_document())

# Undo the last change
text_editor.undo()

print("Document after undo:", text_editor.get_document())