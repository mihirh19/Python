from . import  Stack
import pytest

@pytest.fixture(scope="module")
def setup_stack():
   return Stack()
   
def test___init__(setup_stack):
   
   assert setup_stack._capacity == 10
   assert setup_stack._size == 0
   assert setup_stack._items == [None] * 10

def test_push(setup_stack):
   setup_stack.push(1)
   setup_stack.push(2)
   setup_stack.push(3)
   setup_stack.push(4)
   print(setup_stack)
   assert setup_stack.peek() == 4

def test_pop(setup_stack):
   setup_stack.pop()
   assert setup_stack.peek() == 3

