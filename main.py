import pygame
import sys


def check_win(mas, sing):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sing) == 3:
            return sing
    for col in range(3):
        if mas[0][col] == sing and mas[1][col] == sing and mas[2][col] == sing:
            return sing
    if mas[0][0] == sing and mas[1][1] == sing and mas[2][2] == sing:
        return sing
    if mas[0][2] == sing and mas[1][1] == sing and mas[2][0] == sing:
        return sing
    if zeroes == 0:
        return 'Pies'
    return False


pygame.init()
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size_block = 100
margin = 15
width = heigth = size_block * 3 + margin * 4
size = (width, heigth)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('TicTakToe')
img = pygame.image.load('img/icon.png')
pygame.display.set_icon(img)

mas = [[0] * 3 for i in range(3)]
query = 0
game_over = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'X'
                else:
                    mas[row][col] = 'O'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(BLACK)
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'X':
                    color = RED
                elif mas[row][col] == 'O':
                    color = GREEN
                else:
                    color = WHITE
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == RED:
                    pygame.draw.line(screen, WHITE, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 3)
                    pygame.draw.line(screen, WHITE, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 3)
                elif color == GREEN:
                    pygame.draw.circle(screen, WHITE, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3,
                                       3)
    if (query - 1) % 2 == 0:
        game_over = check_win(mas, 'X')
    else:
        game_over = check_win(mas, 'O')

    if game_over:
        screen.fill(BLACK)
        font = pygame.font.SysFont('stxingkai', 80)
        text1 = font.render(game_over, True, WHITE)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])

    pygame.display.update()

# if __name__ == '__main__':
#     print_hi('PyCharm')
