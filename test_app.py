import unittest
from app import add, multiply, divide, greet


class TestAddFunction(unittest.TestCase):
    """Tests pour les fonctions mathématiques et de salutation."""

    def test_add(self):
        """Test de la fonction add()."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_multiply(self):
        """Test de la fonction multiply()."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        """Test de la fonction divide()."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), None)
        self.assertEqual(divide(0, 5), 0)

    def test_greet(self):
        """Test de la fonction greet()."""
        self.assertEqual(greet("Alice"), "Hello, Alice")
        self.assertEqual(greet(""), "Hello, World!")
        self.assertEqual(greet("Bob"), "Hello, Bob")


if __name__ == "__main__":
    unittest.main()
