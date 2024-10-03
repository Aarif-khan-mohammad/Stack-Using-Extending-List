class Stack(list):

    def is_empty(self):
        return len(self) ==0 #self is object of stack and stack is list's child class
    
    def push(self , data):
        self.append(data)
    
    def pop(self):
        if not self.is_empty():
            super().pop() #self.pop() is not using because, list class its own pop method , when creating pop method here , it create infinate recurrsion , which leads to method overriding. so we are accessing using super of method.
        else:
            raise IndexError("Stack is Empty")
    
    def peek(self):
         if not self.is_empty():
             return self[-1]
         else:
             raise IndexError("Stack is Empty")
         
    def size(self):
        return len(self)
    
    def insert(self,index,data):
        raise AttributeError("No Attribute 'insert' in Stack") #implementing a way to restrict use of insert() method of list class from stack object

s1 = Stack()
#s1.insert(0,10)
# s1.insert(1,20) we can perform insert , so we need to restrict
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print("top value = " , s1.peek()) #top value =  40
print(s1) #[10, 20, 30, 40]