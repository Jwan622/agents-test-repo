import pytest

from tictactoe.board import new_board, place


def test_a_new_board_is_empty() -> None:
    assert new_board() == [[None] * 3 for _ in range(3)]


def test_a_taken_cell_cannot_be_played_again() -> None:
    board = new_board()
    place(board, 0, 0, "X")
    with pytest.raises(ValueError):
        place(board, 0, 0, "O")
