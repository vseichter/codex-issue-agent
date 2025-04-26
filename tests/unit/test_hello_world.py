import io
import sys
import os
import subprocess
import unittest


class TestHelloWorld(unittest.TestCase):
    def test_main_prints_hello_world(self):
        # Capture stdout for main()
        captured = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured
        try:
            from hello_world import main
            main()
        finally:
            sys.stdout = original_stdout
        self.assertEqual(captured.getvalue(), "Hello, World!\n")

    def test_script_outputs_hello_world(self):
        # Test execution of the script via subprocess
        script = os.path.abspath(os.path.join(os.getcwd(), 'hello_world.py'))
        result = subprocess.run(
            [sys.executable, script],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.assertEqual(result.stdout, "Hello, World!\n")
        self.assertEqual(result.stderr, "")


if __name__ == '__main__':
    unittest.main()
