import io
import sys
import unittest

from hello_world import main

class TestHelloWorld(unittest.TestCase):
    def test_main_output(self):
        """Test that main() prints 'Hello, World!' to stdout."""
        captured_out = io.StringIO()
        captured_err = io.StringIO()
        sys_stdout, sys_stderr = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = captured_out, captured_err
            main()
        finally:
            sys.stdout, sys.stderr = sys_stdout, sys.stderr
        self.assertEqual(captured_out.getvalue(), "Hello, World!\n")
        self.assertEqual(captured_err.getvalue(), "")