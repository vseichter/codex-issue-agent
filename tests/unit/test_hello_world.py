import io
import unittest
from contextlib import redirect_stdout
import hello_world


class HelloWorldTest(unittest.TestCase):
    def test_main_output(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            hello_world.main()
        self.assertEqual(buf.getvalue(), "Hello, World!\n")


if __name__ == "__main__":
    unittest.main()