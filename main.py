import pygame

X = 400
Y = 400

white = (255, 255, 255)
black = (0, 0, 0)


class tic_tac_toe:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('TIC TAC TOE')
        self.FPS = 60
        self.wel_type = 0
        self.situation = 'init'
        self.map = []
        self.choice = (0, 0)
        self.clock = pygame.time.Clock()
        self.windows = pygame.display.set_mode((X, Y))
        self.welcome()

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
            text = font.render('Enter', True, black, white)
        else:
            text = font.render('Enter', True, white, black)
        enter_text = text.get_rect()
        enter_text.midleft = (X // 2 - 40, Y // 2 + 30)
        self.windows.blit(text, enter_text)

        if self.wel_type == 0:
            text = font.render('Exit', True, white, black)
        else:
            text = font.render('Exit', True, black, white)

        exit_text = text.get_rect()
        exit_text.midleft = (X // 2 - 40, Y // 2 + 80)
        self.windows.blit(text, exit_text)

    def game_body(self):
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
                    color = black
                if self.map[row][col] != '':
                    symbol = self.map[row][col]
                    font = pygame.font.Font('freesansbold.ttf', 70)
                    text = font.render(symbol, True, color)
                    symbol = text.get_rect()
                    symbol.center = (X // 2 + (col - 1) * 100, Y // 2 + (row - 1) * 100 + 5)
                    self.windows.blit(text, symbol)

    def draw_choice(self):
        row, col = self.choice
        pygame.draw.rect(self.windows, white,
                         pygame.Rect(X // 2 - 40 + (col - 1) * 100, Y // 2 - 37 + (row - 1) * 100, 80, 80))
        pygame.display.flip()

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
                        self.wel_type = 0
                        self.welcome()

                    if key_in[pygame.K_DOWN]:
                        self.wel_type = 1
                        self.welcome()

                    if key_in[pygame.K_RETURN]:
                        if self.wel_type == 0:
                            self.situation = 'body'
                            self.map = [['', '', ''], ['', '', ''], ['', '', '']]

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

                if self.situation == 'body':
                    self.game_body()
                    pygame.display.update()


if __name__ == '__main__':
    game = tic_tac_toe()
    while True:
        game.event_maintain()
        pygame.display.update()
