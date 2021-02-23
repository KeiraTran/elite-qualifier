from main import reply
import unittest
import time

class TestChatBot (unittest.TestCase):
  def raises_exception(self): 
    start_time = time.time()
    with self.assertRaises(Exception):
      reply ("A")
    end_time = time.time()

    elapsed_time = end_time - start_time

    print ("test_perf took" + str(elapsed_time) + "seconds.")

    self.assertTrue (elapsed_time < 10)

if __name__ == '__main__': 
  unittest.main()