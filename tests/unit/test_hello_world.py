"""Unit tests for hello_world.py."""

import contextlib
import subprocess
import sys
import unittest
from io import StringIO

import hello_world


class TestHelloWorld(unittest.TestCase):
    def test_main_prints_hello_world(self):
        buf = StringIO()
        with contextlib.redirect_stdout(buf):
            hello_world.main()
        self.assertEqual(buf.getvalue(), "Hello, World!\n")

    def test_script_output(self):
        result = subprocess.run(
            [sys.executable, "hello_world.py"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.stdout, "Hello, World!\n")
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()