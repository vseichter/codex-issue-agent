import io
from contextlib import redirect_stdout
import unittest
from hello_world import main

class TestHelloWorld(unittest.TestCase):
    def test_main_output(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            main()
        self.assertEqual(buf.getvalue(), "Hello, World!\n")

if __name__ == "__main__":
    unittest.main()
