from . import circular_linked_list as cll

l1 = cll.CircularLinkedList()

def test_insert_head():
   l1.insert_head(1)
   assert l1.head.data == 1

def test_insert_tail():
   l1.insert_tail(2)
   assert l1.tail.data == 2

def test_insert_at_index():
   l1.insert_at_index(1, 3)
   assert l1.head.next.data == 3