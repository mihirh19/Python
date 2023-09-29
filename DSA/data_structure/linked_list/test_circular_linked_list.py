import pytest
from . import circular_linked_list as cll


@pytest.fixture(scope="module")
def init_link():
   return cll.CircularLinkedList()
def test_insert_head(init_link):
   init_link.insert_head(1)
   assert init_link.head.data == 1

def test_insert_tail(init_link):
   init_link.insert_tail(2)
   assert init_link.tail.data == 2

def test_insert_at_index(init_link):
   init_link.insert_at_index(1, 3)
   assert init_link.head.next.data == 3