import os
from math import pi, pow

# ========== Math Module ============
print(pi)

result = pow(2, 2)
print("Result: ", result)

# ========== OS Module ============
print(os.name)  # os name
print(os.getcwd())  # current directory

print(os.listdir())  # list all files and directories

# Environment variables
print(os.environ['HOME'])

class TestClass:
    """TestClass
    Stores value _x and increments it by 1
    when TestClass.increment() is called.
    """

    def __init__(self):
        """Initialize TestClass"""
        self._x = 1

    def increment(self):
        """Increment method."""
        self._x += 1

object1 = TestClass()
object2 = TestClass()

object1.increment()

print(object1._x)
print(object2._x)

def test(message):
    print(f"""
        {message}
        {__name__}
    """)

import sys

print(sys.argv)
print(sys.executable) 
print(sys.path) 
print(sys.version)
print(sys.platform)


if __name__ == "__main__":
    test("Hello World!")

