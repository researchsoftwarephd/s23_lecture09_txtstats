"""Tests for the CLI module."""

import re
import sys

from txtstats.cli import _main


def test_main_output(tmp_path, capsys, monkeypatch, data_to_test):
    """Test the print function prints to the console."""
    # Create a temporary file with data in string_to_test
    file = tmp_path / "file_to_test.txt"
    file.write_text(data_to_test[0])
    # Specify a that temporary file as a command line argument
    monkeypatch.setattr(sys, "argv", [sys.argv[0], str(file)])
    # Run the function called when the txtstats console command is invoked
    _main()
    # Capture the output printed to the console by the previous command
    output = capsys.readouterr().out.rstrip()
    # Check that the command produces the expected output
    for stat_name in data_to_test[1]:
        assert re.search(f"{stat_name}(.*){data_to_test[1][stat_name]}", output)
