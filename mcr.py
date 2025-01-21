72402014  72403164 72402260 72401607


```python
def check_winner(game, player):
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] == player:
            return True
        if game[0][i] == game[1][i] == game[2][i] == player:
            return True
    if game[0][0] == game[1][1] == game[2][2] == player:
        return True
    if game[0][2] == game[1][1] == game[2][0] == player:
        return True
    return False

def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    is_player1_turn = True

    print("X = Player 1")
    print("O = Player 2")

    for _ in range(9):
        is_player1_turn = not is_player1_turn
        player = player1 if is_player1_turn else player2
        print(f"Player {('1' if is_player1_turn else '2')}: ", end="")
        print("Which cell to mark? i:[1..3], j:[1..3]: ", end=" ")
        i, j = map(int, input().split())
        i -= 1
        j -= 1

        if game[i][j] != ' ':
            print("This cell is already marked. Choose another one.")
            continue

        game[i][j] = player

        if check_winner(game, player):
            print("Win!")
            break

        if _ == 8:  # All cells have been filled
            print("Tie!")

        for row in game:
            print(" ".join(row))

if __name__ == "__main__":
    main()
```
