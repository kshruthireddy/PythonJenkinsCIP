import unittest
from app import add, subtract

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

if __name__ == "__main__":
    unittest.main()