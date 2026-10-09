import pytest

from tictactoe.board import new_board, place, winner


def test_a_new_board_is_empty() -> None:
    assert new_board() == [[None] * 3 for _ in range(3)]


def test_a_taken_cell_cannot_be_played_again() -> None:
    board = new_board()
    place(board, 0, 0, "X")
    with pytest.raises(ValueError):
        place(board, 0, 0, "O")


def board_with(mark: str, cells: list[tuple[int, int]]) -> list[list[str | None]]:
    """A literal-style grid where only the given (row, col) cells hold `mark`."""
    grid: list[list[str | None]] = [[None] * 3 for _ in range(3)]
    for row, col in cells:
        grid[row][col] = mark
    return grid


@pytest.mark.parametrize(
    ("board", "expected"),
    [
        pytest.param(board_with(mark, [(row, c) for c in range(3)]), mark, id=f"row_{row}_{mark}")
        for row in range(3)
        for mark in ("X", "O")
    ]
    + [
        pytest.param([["X", "X", None], ["O", "O", "O"], ["X", None, None]], "O", id="o_row_beside_x_marks"),
        pytest.param([["X", "X", "X"], ["O", "O", None], [None, None, None]], "X", id="x_row_beside_o_marks"),
    ],
)
def test_full_row_returns_that_mark(board: list[list[str | None]], expected: str) -> None:
    before = [list(row) for row in board]

    assert winner(board) == expected
    assert board == before


@pytest.mark.parametrize(
    ("board", "expected"),
    [
        pytest.param(board_with(mark, [(r, col) for r in range(3)]), mark, id=f"column_{col}_{mark}")
        for col in range(3)
        for mark in ("X", "O")
    ]
    + [
        pytest.param([["O", "X", None], ["O", "X", "O"], ["O", None, "X"]], "O", id="o_column_beside_x_marks"),
        pytest.param([["X", "O", None], ["X", "O", None], ["X", None, "O"]], "X", id="x_column_beside_o_marks"),
    ],
)
def test_full_column_returns_that_mark(board: list[list[str | None]], expected: str) -> None:
    assert winner(board) == expected


@pytest.mark.parametrize(
    ("board", "expected"),
    [
        pytest.param(board_with(mark, [(i, i) for i in range(3)]), mark, id=f"main_diagonal_{mark}")
        for mark in ("X", "O")
    ]
    + [
        pytest.param(board_with(mark, [(i, 2 - i) for i in range(3)]), mark, id=f"anti_diagonal_{mark}")
        for mark in ("X", "O")
    ]
    + [
        pytest.param([["X", "O", None], ["O", "X", None], [None, None, "X"]], "X", id="x_main_diagonal_beside_o_marks"),
        pytest.param([["X", "X", "O"], [None, "O", None], ["O", None, "X"]], "O", id="o_anti_diagonal_beside_x_marks"),
    ],
)
def test_full_diagonal_returns_that_mark(board: list[list[str | None]], expected: str) -> None:
    assert winner(board) == expected


def test_empty_board_has_no_winner() -> None:
    assert winner([[None] * 3 for _ in range(3)]) is None


def test_full_drawn_board_has_no_winner() -> None:
    assert winner([["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]) is None


@pytest.mark.parametrize(
    "board",
    [
        pytest.param([["X", "X", None], ["O", "O", None], [None, None, None]], id="two_in_a_row_plus_empty_cell"),
        pytest.param([["X", "O", "X"], [None, None, None], [None, None, None]], id="full_row_mixing_x_and_o"),
        pytest.param([["X", None, None], ["X", None, None], ["O", None, None]], id="column_with_blocker"),
        pytest.param([["X", None, None], [None, "X", None], [None, None, "O"]], id="diagonal_with_blocker"),
    ],
)
def test_in_progress_board_without_line_has_no_winner(board: list[list[str | None]]) -> None:
    assert winner(board) is None
