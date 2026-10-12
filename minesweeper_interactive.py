import random


def mines(n):
    # Build an n x n board of 'o' (empty) and place the mines
    k = []
    d = (n**2)//2 + random.randint(0, n)
    d = min(d, n*n - 1)   # never ask for more mines than squares (leave one safe)
    for ik in range(n):
        k.append(['o'] * n)

    l = set()
    while len(l) < d:
        a = (random.randint(0, n-1), random.randint(0, n-1))
        if a not in l:
            l.add(a)
            k[a[0]][a[1]] = 'x'

    # Replace every non-mine square with the number of mines around it
    for i in range(n):
        for j in range(n):
            if k[i][j] == 'x':
                continue
            k[i][j] = str(sum(1 for r, c in neighbours(i, j, n) if k[r][c] == 'x'))
    return k


def neighbours(i, j, n):
    loki = []
    for r in range(i-1, i+2):
        for c in range(j-1, j+2):
            if (r, c) != (i, j) and 0 <= r < n and 0 <= c < n:
                loki.append((r, c))
    return loki


def show(k, seen, flags, reveal_all=False):
    n = len(k)
    print('     ' + ''.join(f'{c:<4}' for c in range(n)))
    for i in range(n):
        row = f'{i:<4} '
        for j in range(n):
            if reveal_all or (i, j) in seen:
                cell = '.' if k[i][j] == '0' else k[i][j]
            elif (i, j) in flags:
                cell = 'F'
            else:
                cell = '#'
            row += f'{cell:<4}'
        print(row)
    print()


def open_square(k, seen, i, j):
    # Reveal a square; if it's a 0, keep opening its neighbours
    n = len(k)
    todo = [(i, j)]
    while todo:
        r, c = todo.pop()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        if k[r][c] == '0':
            todo.extend(p for p in neighbours(r, c, n) if p not in seen)


def play(n):
    k = mines(n)
    total_mines = sum(row.count('x') for row in k)
    seen, flags = set(), set()
    print(f'{n}x{n} board, {total_mines} mines.')
    print("Type 'row col' to open a square, 'f row col' to flag/unflag, 'q' to quit.\n")

    while True:
        show(k, seen, flags)
        move = input('Your move: ').strip().lower().split()
        if move == ['q']:
            print('Coward.')
            show(k, seen, flags, reveal_all=True)
            return

        flag = bool(move) and move[0] == 'f'
        if flag:
            move = move[1:]
        try:
            i, j = int(move[0]), int(move[1])
            if not (0 <= i < n and 0 <= j < n) or len(move) != 2:
                raise ValueError
        except (ValueError, IndexError):
            print(f'Give a row and column between 0 and {n-1}, e.g. "3 4" or "f 3 4".\n')
            continue

        if flag:
            if (i, j) in seen:
                print('That square is already open.\n')
            else:
                flags ^= {(i, j)}
            continue

        if (i, j) in flags:
            print('That square is flagged. Unflag it first with "f row col".\n')
            continue

        # Your first click is never a mine: reroll the board until it's safe
        while not seen and k[i][j] == 'x':
            k = mines(n)
            total_mines = sum(row.count('x') for row in k)

        if k[i][j] == 'x':
            print('BOOM! You hit a mine.\n')
            show(k, seen, flags, reveal_all=True)
            return

        open_square(k, seen, i, j)
        if len(seen) == n*n - total_mines:
            print('You cleared the board. You win!\n')
            show(k, seen, flags, reveal_all=True)
            return


# Edit this for difficulty
while True:
    a = input('Choose your difficulty :- \n1. Human \n2. Deity \n3. God \n')
    if a == '1' or a.lower() == 'human':
        play(7)
    elif a == '2' or a.lower() == 'deity':
        play(9)
    elif a == '3' or a.lower() == 'god':
        play(13)
    else:
        print('Get your eyes checked moron')
        continue

    if input('Play again? (y/n) ').strip().lower() != 'y':
        break
