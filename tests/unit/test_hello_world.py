"""
Unit tests for hello_world.py using unittest.
"""

import io
import unittest
from contextlib import redirect_stdout
from hello_world import main


class TestHelloWorld(unittest.TestCase):
    def test_main_prints_hello_world(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            main()
        self.assertEqual(buffer.getvalue(), "Hello, World!\n")


if __name__ == "__main__":
    unittest.main()