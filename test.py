from main import reply
import unittest

class TestChatBot (unittest.TestCase):
  def raises_exception(self): 
    with self.assertRaises(Exception):
      reply ("A")


if __name__ == '__main__': 
  unittest.main()