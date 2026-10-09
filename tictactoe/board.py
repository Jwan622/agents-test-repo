"""A tic-tac-toe board: 3x3 cells, each "X", "O", or None."""

from __future__ import annotations

Cell = str | None
Board = list[list[Cell]]


def new_board() -> Board:
    return [[None] * 3 for _ in range(3)]


def place(board: Board, row: int, col: int, mark: str) -> None:
    if mark not in ("X", "O"):
        raise ValueError(f"mark must be X or O, got {mark!r}")
    if board[row][col] is not None:
        raise ValueError(f"cell ({row}, {col}) is taken")
    board[row][col] = mark


_LINES = (
    # rows
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    # columns
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    # diagonals
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
)


def winner(board: Board) -> Cell:
    """Return "X" or "O" if that mark fills a row, column, or diagonal, else None.

    Reads the board without changing it. If two different lines are complete
    (not a legal game), the first one in `_LINES` wins.
    """
    for line in _LINES:
        first, second, third = (board[row][col] for row, col in line)
        if first is not None and first == second == third:
            return first
    return None
