from constructors_2 import Rectangle

def test_constructors_2():
   
   # Create objects of the Rectangle class
   rect1 = Rectangle(5, 10)
   rect2 = Rectangle(3, 7)
   assert rect1.width == 5
   assert rect1.height == 10
   assert rect2.width == 3
   assert rect2.height == 7
   assert rect1.area() == 50
   assert rect1.perimeter() == 30
   assert rect2.area() == 21
   assert rect2.perimeter() == 20
