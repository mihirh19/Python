from . import  Stack
s = Stack()
def test___init__():
   
   assert s._capacity == 10
   assert s._size == 0
   assert s._items == [None] * 10

def test_push():
   s.push(1)
   s.push(2)
   s.push(3)
   s.push(4)
   print(s)
   assert s.peek() == 4

def test_pop():
   s.pop()
   assert s.peek() == 3

