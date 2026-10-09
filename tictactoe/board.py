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
