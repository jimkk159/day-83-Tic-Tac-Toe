import random

import pygame
from random import choice
from itertools import combinations

X = 400
Y = 400

white = (255, 255, 255)
black = (0, 0, 0)


class TicTacToe:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('TIC TAC TOE')
        self.blink_color = [black, white]
        self.choice = (0, 0)
        self.clock = pygame.time.Clock()
        self.count = 0
        self.FPS = 60
        self.map = []
        self.wel_type = 0
        self.situation = 'init'
        self.turn = 'Human'
        self.turn_to = 'Human'
        self.winner = ''
        self.windows = pygame.display.set_mode((X, Y))
        self.welcome()

    def reset_map(self):
        self.map = [['', '', ''], ['', '', ''], ['', '', '']]

    def color_blink(self):
        self.count += 1
        if self.count == 50:
            self.blink_color = (self.blink_color[1], self.blink_color[0])

        if self.count == 60:
            self.count = 0

    def switch_turn(self):
        if self.turn != self.turn_to:
            self.turn = self.turn_to

    # For Game Start View
    def welcome(self):
        self.windows.fill(black)
        font = pygame.font.Font('freesansbold.ttf', 44)
        text = font.render('Welcome to', True, white)
        welcome_text = text.get_rect()
        welcome_text.center = (X // 2, Y // 2 - 100)
        self.windows.blit(text, welcome_text)

        font = pygame.font.Font('freesansbold.ttf', 28)
        text = font.render('Tic Tac Toe Game!', True, white)
        welcome_text = text.get_rect()
        welcome_text.center = (X // 2, Y // 2 - 50)
        self.windows.blit(text, welcome_text)

        font = pygame.font.Font('freesansbold.ttf', 28)
        if self.wel_type == 0:
            text = font.render('Enter', True, self.blink_color[0], self.blink_color[1])
        else:
            text = font.render('Enter', True, white, black)
        enter_text = text.get_rect()
        enter_text.midleft = (X // 2 - 40, Y // 2 + 30)
        self.windows.blit(text, enter_text)

        if self.wel_type == 1:
            text = font.render('Exit', True, self.blink_color[0], self.blink_color[1])
        else:
            text = font.render('Exit', True, white, black)

        exit_text = text.get_rect()
        exit_text.midleft = (X // 2 - 40, Y // 2 + 80)
        self.windows.blit(text, exit_text)

    # For Game End
    def ending(self):
        pygame.draw.rect(self.windows, black,
                         pygame.Rect(X // 2 - 100, Y // 2 - 30, 200, 60))
        font = pygame.font.Font('freesansbold.ttf', 44)

        if self.winner == 'Human':
            text = font.render('You Win!', True, white, black)
        elif self.winner == 'AI':
            text = font.render('You Lose!', True, white, black)
        else:
            text = font.render('Tie!!', True, white, black)
        ending_text = text.get_rect()
        ending_text.center = (X // 2, Y // 2)
        self.windows.blit(text, ending_text)

        pygame.draw.rect(self.windows, black,
                         pygame.Rect(X // 2 - 120, Y // 2 + 35, 240, 30))
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('Press Enter to continue', True, self.blink_color[0], black)
        ending_text = text.get_rect()
        ending_text.center = (X // 2, Y // 2 + 50)
        self.windows.blit(text, ending_text)

    def is_end(self):
        rows = len(self.map)
        cols = len(self.map[0])
        for row in range(rows):
            if self.map[row].count('O') == 3:
                self.situation = 'end'
                self.winner = 'Human'
                return

            elif self.map[row].count('X') == 3:
                self.situation = 'end'
                self.winner = 'AI'
                return

        for col in range(cols):
            column = [item[col] for item in self.map]
            if column.count('O') == 3:
                self.situation = 'end'
                self.winner = 'Human'
                return

            elif column.count('X') == 3:
                self.situation = 'end'
                self.winner = 'AI'
                return

        if self.map[1][1] == 'O' and (self.map[0][0] == self.map[1][1] == self.map[2][2] or
                                      self.map[0][2] == self.map[1][1] == self.map[2][0]):
            self.situation = 'end'
            self.winner = 'Human'
            return

        if self.map[1][1] == 'X' and (self.map[0][0] == self.map[1][1] == self.map[2][2] or
                                      self.map[0][2] == self.map[1][1] == self.map[2][0]):
            self.situation = 'end'
            self.winner = 'AI'
            return

        if all(self.map[0]) and all(self.map[1]) and all(self.map[2]):
            print(1)
            self.situation = 'end'
            return

    # For Tic Tac Toe board
    def game_board(self):
        self.windows.fill(black)
        self.draw_title(X - 90, 20)
        self.draw_dash_line(X // 2, Y // 2 + 50)
        self.draw_dash_line(X // 2, Y // 2 - 50)
        self.draw_horizontal_line(X // 2 + 50, Y // 2)
        self.draw_horizontal_line(X // 2 - 50, Y // 2)
        self.draw_choice()
        self.draw_symbol()

    def draw_title(self, x, y):
        title = 'You:O  enemy:X'
        font = pygame.font.Font('freesansbold.ttf', 18)
        text = font.render(title, True, white)
        title = text.get_rect()
        title.center = (x, y)
        self.windows.blit(text, title)

    def draw_symbol(self):
        rows = len(self.map)
        cols = len(self.map[0])
        for row in range(rows):
            for col in range(cols):
                color = white
                if self.choice == (row, col):
                    color = self.blink_color[0]
                if self.map[row][col] != '':
                    symbol = self.map[row][col]
                    font = pygame.font.Font('freesansbold.ttf', 70)
                    text = font.render(symbol, True, color, )
                    symbol = text.get_rect()
                    symbol.center = (X // 2 + (col - 1) * 100, Y // 2 + (row - 1) * 100 + 5)
                    self.windows.blit(text, symbol)

    def draw_choice(self):
        row, col = self.choice
        pygame.draw.rect(self.windows, self.blink_color[1],
                         pygame.Rect(X // 2 - 40 + (col - 1) * 100, Y // 2 - 37 + (row - 1) * 100, 80, 80))

    def draw_dash_line(self, x, y):
        bottom_line = '- ' * 12
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render(bottom_line, True, white)
        bottom_line = text.get_rect()
        bottom_line.center = (x, y)
        self.windows.blit(text, bottom_line)

    def draw_horizontal_line(self, x, y):
        for item in range(6):
            horizontal_line = '|'
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(horizontal_line, True, white)
            horizontal_line = text.get_rect()
            horizontal_line.center = (x, y - 125 + item * 50)
            self.windows.blit(text, horizontal_line)

    def AI_brain(self):
        rows = len(self.map)
        cols = len(self.map[0])

        def check_diagonal(diagonal_list, symbol):
            diag_combine = combinations(diagonal_list, 2)
            for grid1, grid2 in diag_combine:
                if self.map[grid1[0]][grid1[1]] == self.map[grid2[0]][grid2[1]] == symbol:
                    diagonal_list.remove((grid1[0], grid1[1]))
                    diagonal_list.remove((grid2[0], grid2[1]))
                    if self.map[diagonal_list[0][0]][diagonal_list[0][1]] == '':
                        return diagonal_list[0]
                    else:
                        break

        def one_step_win(symbol):

            anti_symbol = ''
            if symbol == 'O':
                anti_symbol = 'X'
            elif symbol == 'X':
                anti_symbol = 'O'

            for row in range(rows):
                if self.map[row].count(symbol) == 2 and self.map[row].count(anti_symbol) == 0:
                    for col in range(cols):
                        if self.map[row][col] != symbol:
                            return row, col

            for col in range(cols):
                array = [item[col] for item in self.map]
                if array.count(symbol) == 2 and array.count(anti_symbol) == 0:
                    for row in range(rows):
                        if self.map[row][col] != symbol:
                            return row, col

            # Positive Diagonal
            pos_dia = [(0, 0), (1, 1), (2, 2)]
            result = check_diagonal(pos_dia, symbol)
            if result:
                return result

            # Negative Diagonal
            neg_dia = [(0, 2), (1, 1), (2, 0)]
            result = check_diagonal(neg_dia, symbol)
            if result:
                return result

        # to win
        result = one_step_win('X')
        if result:
            return result
        # defend
        result = one_step_win('O')
        if result:
            return result

        # to choice
        # First choice middle
        if self.map[1][1] == '':
            return 1, 1

        # Second choice observe enemy
        cross = [(0, 1), (1, 0), (1, 2), (2, 1)]
        corner = [(0, 0), (2, 0), (0, 2), (2, 2)]
        if corner.count('O') > 1:
            pick = random.choice(cross)
            if self.map[pick[0]][pick[1]] == '':
                return pick

        if corner.count('O') == 1:
            for item in cross:
                if self.map[item[0]][item[1]] == 'O':

                    if item[0] == 1:
                        pick_choices = [(item[0] - 1, item[1]), (item[0] + 1, item[1])]
                        return random.choice(pick_choices)

                    if item[1] == 1:
                        pick_choices = [(item[0], item[1] - 1), (item[0], item[1] + 1)]
                        return random.choice(pick_choices)

        rest_corner = corner.copy()
        count = 0
        col_set = [0, 1, 2]
        row_set = [0, 1, 2]
        for item in cross:
            if self.map[item[0]][item[1]] == 'O':

                if count == 0:
                    col_set.remove(item[0])
                    row_set.remove(item[1])
                    count += 1

                elif item[0] in col_set and item[1] in row_set:
                    col_set.remove(item[0])
                    row_set.remove(item[1])
                    rest_corner.remove((col_set[0], row_set[0]))
                    pick_row, pick_col = random.choice(rest_corner)
                    if self.map[pick_row][pick_col] == '':
                        return pick_row, pick_col

        # Third choice corner
        for item in corner:
            if self.map[item[0]][item[1]] == '':
                return item

        # Third choice cross
        for item in cross:
            if self.map[item[0]][item[1]] == '':
                return item

    # For input event deal with
    def event_maintain(self):

        self.clock.tick(self.FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                key_in = pygame.key.get_pressed()
                if self.situation == 'init':

                    if key_in[pygame.K_UP]:
                        self.count = 0
                        self.blink_color = [black, white]
                        self.wel_type = 0

                    if key_in[pygame.K_DOWN]:
                        self.blink_color = [black, white]
                        self.count = 0
                        self.wel_type = 1

                    if key_in[pygame.K_RETURN]:
                        if self.wel_type == 0:
                            self.situation = 'body'
                            self.reset_map()

                        elif self.wel_type == 1:
                            pygame.quit()
                            quit()

                elif self.situation == 'body':

                    row, col = self.choice
                    if key_in[pygame.K_UP]:
                        row -= 1
                        if row < 0:
                            row = 1
                        self.choice = row, col

                    elif key_in[pygame.K_DOWN]:
                        row += 1
                        if row > 2:
                            row = 2
                        self.choice = row, col

                    elif key_in[pygame.K_LEFT]:
                        col -= 1
                        if col < 0:
                            col = 0
                        self.choice = row, col

                    elif key_in[pygame.K_RIGHT]:
                        col += 1
                        if col > 2:
                            col = 2
                        self.choice = row, col

                    elif key_in[pygame.K_RETURN]:
                        row, col = self.choice
                        if self.map[row][col] == '':
                            self.map[row][col] = 'O'
                            self.turn_to = 'AI'

                elif self.situation == 'end':
                    if key_in[pygame.K_RETURN]:
                        # reset variable
                        self.situation = 'body'
                        self.turn = 'Human'
                        self.turn_to = 'Human'
                        self.winner = ''
                        self.reset_map()

        if self.situation == 'init':
            self.welcome()

        if self.turn == self.turn_to == 'AI' and self.situation == 'body':
            ai_choice = self.AI_brain()
            self.map[ai_choice[0]][ai_choice[1]] = 'X'
            self.turn_to = 'Human'

        if self.situation == 'body':
            self.game_board()
            self.is_end()
            self.switch_turn()

        if self.situation == 'end':
            self.ending()

        self.color_blink()
        pygame.display.update()


if __name__ == '__main__':
    game = TicTacToe()
    while True:
        game.event_maintain()
        pygame.display.update()
