class stack:
     def __init__(self, l):
          self.stack_list = []
          self.limit = l 
          
     def push_method(self, val):
          len_stack = len(self.stack_list)
          if(len_stack < self.limit):
               self.stack_list.append(val)
          else:
               print("stack over flow")
               
     def pop_method(self):
          if(len(self.stack_list) != 0):
               self.stack_list.pop()
          else:
               print("stack under flow")
               
     def peak_method(self):
          if (len(self.stack_list) !=0):
               print(self.stack_list[-1])
          else:
               print("stack is empty")
               
               
stack_1 = stack(3)

while(True):
     print("select an option 1.push 2.pop 3.peak 4.exit")
     n = int(input("Choose an option: "))
     if(n == 1):
          num = int(input("Enter the number: "))
          stack_1.push_method(num)
     elif(n == 2):
          stack_1.pop_method()
     elif(n == 3):
          stack_1.peak_method()
     elif(n == 4):
          break
     else:
          print("Invalid input")