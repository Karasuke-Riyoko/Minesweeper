# Minesweeper

A tiny Minesweeper written in Python by **kyuerm**. Pick a difficulty and it generates a random minefield for you.

There are two versions in this repo:

| File | What it does |
| --- | --- |
| `minesweeper.py` | The original script. It builds a random board, prints where the mines are, then prints the finished board with every number filled in. |
| `minesweeper_interactive.py` | A playable version of the same game. Open squares, flag mines, and try to clear the board without blowing up. |

## Difficulties

Each board is square, and roughly half of it is mines (n²/2 plus a random extra of up to n).

| # | Name | Board | Mines |
| --- | --- | --- | --- |
| 1 | Human | 7 × 7 | 24 to 31 |
| 2 | Deity | 9 × 9 | 40 to 49 |
| 3 | God | 13 × 13 | 84 to 97 |

Type the number or the name when it asks. Type anything else and it will tell you to get your eyes checked.

## How to run

You need Python 3. No extra packages.

**Original board generator**

```bash
python minesweeper.py
```

It keeps asking for a difficulty after each board. Press `Ctrl+C` to stop.

**Playable version**

```bash
python minesweeper_interactive.py
```

Controls:

- `3 4` opens the square at row 3, column 4
- `f 3 4` flags or unflags that square
- `q` gives up and shows the whole board

Your first move is never a mine. Opening a `0` square (shown as `.`) automatically opens everything around it. You win when every safe square is open.

On some systems the command is `python3` instead of `python`.

## Sample board

A Human (7 × 7) board from `minesweeper.py`. First it shows where the mines are (`x`) and empty squares (`o`):

```
x    x    o    o    x    o    x
o    o    x    x    o    o    x
o    x    x    o    o    o    x
x    x    x    x    x    x    o
x    x    x    o    x    x    o
x    o    o    x    o    x    o
x    o    o    o    x    o    o
```

Then the solved board, where each number is how many mines touch that square:

```
x    x    3    3    x    3    x
3    5    x    x    2    4    x
3    x    x    6    4    4    x
x    x    x    x    x    x    3
x    x    x    6    x    x    3
x    5    3    x    5    x    2
x    2    1    2    x    2    1
```

## Author

Made by **kyuerm**.
