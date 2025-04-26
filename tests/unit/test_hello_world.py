import subprocess
import sys

from hello_world import main


def test_main_prints_hello_world(capsys):
    """main() should print 'Hello, World!' to stdout."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"


def test_script_execution_outputs_hello_world():
    """Running the script should output 'Hello, World!' and exit with code 0."""
    result = subprocess.run([sys.executable, "hello_world.py"], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout == "Hello, World!\n"
    assert result.stderr == ""