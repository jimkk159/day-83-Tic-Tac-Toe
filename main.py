import pygame

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
        self.windows = pygame.display.set_mode((X, Y))
        self.welcome()

    def reset_map(self):
        self.map = [['', '', ''], ['', '', ''], ['', '', '']]

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

    def ending(self):
        pygame.draw.rect(self.windows, black,
                         pygame.Rect(X // 2 - 100, Y // 2 - 30, 200, 60))
        font = pygame.font.Font('freesansbold.ttf', 44)
        if self.turn == 'Human':
            text = font.render('You Win!', True, white, black)
        else:
            text = font.render('You Lose!', True, white, black)
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
            if self.map[row].count('O') == 3 or self.map[row].count('X') == 3:
                self.situation = 'end'

        for col in range(cols):
            column = [item[col] for item in self.map]
            if column.count('O') == 3 or column.count('X') == 3:
                self.situation = 'end'

        if (self.map[1][1] == 'O' or self.map[1][1] == 'X') and \
                (self.map[0][0] == self.map[1][1] == self.map[2][2] or
                 self.map[0][2] == self.map[1][1] == self.map[2][0]):
            self.situation = 'end'

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

    def color_blink(self):
        self.count += 1
        if self.count == 50:
            self.blink_color = (self.blink_color[1], self.blink_color[0])

        if self.count == 60:
            self.count = 0

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
                            self.map = [['X', '', ''], ['X', '', ''], ['X', '', '']]

                        elif self.wel_type == 1:
                            pygame.quit()
                            quit()

                elif self.situation == 'body':

                    if self.turn == 'Human':
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
                                # self.turn = 'AI'

                elif self.situation == 'end':
                    print(1)
                    if key_in[pygame.K_RETURN]:
                        self.situation = 'body'
                        self.reset_map()
                    # elif self.turn == 'AI':
                    #     rows = len(self.map)
                    #     cols = len(self.map[0])
                    #     # defend
                    #     for row in rows:
                    #         if self.map[row].count('O') == 2:
                    #             for col in cols:
                    #                 ai_choice = (row, col)
                    #     for col in cols:
                    #         if self.map[row].count('O') == 2:
                    #             for row in rows:
                    #                 ai_choice = (row, col)

        if self.situation == 'init':
            self.welcome()

        if self.situation == 'body':
            self.game_board()
            self.is_end()

        if self.situation == 'end':
            self.ending()

        self.color_blink()
        pygame.display.update()


if __name__ == '__main__':
    game = TicTacToe()
    while True:
        game.event_maintain()
        pygame.display.update()
