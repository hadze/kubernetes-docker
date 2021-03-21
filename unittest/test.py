import unittest
from main import hello_world, get_version

class TestStringMethods(unittest.TestCase):

    def test_hello(self):
        expected = "Hello world!"
        result = hello_world()
        self.assertEqual(result, expected)
        
    def test_version(self):
        expected = 'This is Python version: 3'
        result = get_version()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()