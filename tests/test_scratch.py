import importlib


def test_scratch_module_docstring_marks_it_as_removable() -> None:
    scratch = importlib.import_module("tictactoe.scratch")

    assert scratch.__doc__ == "Scratch file for testing the agent pipeline. Safe to delete."
