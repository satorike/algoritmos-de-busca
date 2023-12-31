from AprofundamentoIterativo import AprofundamentoIterativo
from astar import Astar
import numpy as np


class ConnectFour:
    def __init__(self, board):
        self.board = board
        self.current_player = 'X'
        self.turn_count = 42

    def print_board(self):
        for row in self.board:
            print(row)
        print("_" * 54)

    def make_move(self, column):
        for i in range(5, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.current_player
                break
        else:
            print("Coluna cheia")
            return False

        return True

    def check_winner(self):
        for row in self.board:
            if 'XXXX' in ''.join(row) or 'OOOO' in ''.join(row):
                return True

        for col in range(7):
            column = ''.join(self.board[row][col] for row in range(6))
            if 'XXXX' in column or 'OOOO' in column:
                return True

        for i in range(3):
            for j in range(4):
                if (self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] == 'X' or
                        self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] == 'O'):
                    return True

        for i in range(3):
            for j in range(3, 7):
                if (self.board[i][j] == self.board[i + 1][j - 1] == self.board[i + 2][j - 2] == self.board[i + 3][j - 3] == 'X' or
                        self.board[i][j] == self.board[i + 1][j - 1] == self.board[i + 2][j - 2] == self.board[i + 3][j - 3] == 'O'):
                    return True

        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self, player1, player2):
        while self.turn_count:
            self.print_board()

            try:
                if self.current_player == 'X':
                    # column = Astar(self.board).astar()
                    # column = AprofundamentoIterativo(self.board).busca()
                    if player1 == 'I':
                        column = AprofundamentoIterativo(self.board).busca()
                    elif player1 == 'A':
                        column = Astar(self.board).astar()
                    else:
                        column = int(input(f"Jogador {self.current_player}, escolha uma coluna (1-7): ")) - 1
                else:
                    # column = Astar(self.board).astar()
                    # column = AprofundamentoIterativo(self.board).busca()
                    if player2 == 'I':
                        column = AprofundamentoIterativo(self.board).busca()
                    elif player2 == 'A':
                        column = Astar(self.board).astar()
                    else:
                        column = int(input(f"Jogar {self.current_player}, escolha uma coluna (1-7): ")) - 1

                if 0 <= column <= 6:
                    if self.make_move(column):
                        if self.check_winner():
                            self.print_board()
                            print(f"Jogador {self.current_player} ganhou!")
                            break
                        self.switch_player()
                    else:
                        continue
                else:
                    print("Coluna invalida")
                self.turn_count -= 1
            except ValueError:
                print("Entrada invalida")
        
        if self.turn_count == 0:
            print("Empate")


def main():
    board = np.full((6, 7), ' ', dtype='str')
    game = ConnectFour(board)
    player1, player2 = '', ''
    player1 = input(f'Primeiro jogador: (A/I/H):')
    player2 = input(f'Segundo jogador: (A/I/H):')
    game.play_game(player1=player1, player2=player2)


if __name__ == '__main__':
    main()
