import pygame as pg

pg.init()


def check_winners(mas, sing):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sing) == 3:
            return sing
            print(1)
    for col in range(3):
        if mas[0][col] == sing and mas[1][col] == sing and mas[2][col] == sing:
            return sing
    if mas[0][0] == sing and mas[1][1] == sing and mas[2][2] == sing:
        return sing
    if mas[0][2] == sing and mas[1][1] == sing and mas[2][0] == sing:
        return sing
    if zeroes == 0:
        return 'Ничья'
    return False


sizeblock = 100
margine = 15

WIDTH = HEIGTH = sizeblock * 3 + margine * 4
RES = WIDTH, HEIGTH

sc = pg.display.set_mode(RES)
pg.display.set_caption('Крестики нолики!')

clock = pg.time.Clock()

FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_2 = (252, 255, 255)
WHITE_3 = (251, 255, 255)
NASROZOVI = (0, 0, 0)
ORHID = (0, 0, 0)

mas = [[0] * 3 for i in range(3)]
query = 0

while True:
    sc.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pg.mouse.get_pos()
            col = x_mouse // (sizeblock + margine)
            row = y_mouse // (sizeblock + margine)
            if mas[col][row] == 0:
                if query % 2 == 0:
                    mas[col][row] = 'x'
                else:
                    mas[col][row] = 'o'
                query += 1

    for row in range(3):
        for col in range(3):
            if mas[col][row] == 'x':
                color = WHITE_3
            elif mas[col][row] == 'o':
                color = WHITE_2
            else:
                color = WHITE
            x = col * sizeblock + (col + 1) * margine
            y = row * sizeblock + (row + 1) * margine
            pg.draw.rect(sc, color, (x, y, sizeblock, sizeblock))
            if color == WHITE_3:
                pg.draw.line(sc, NASROZOVI, (x + 10, y + 10), (x + sizeblock - 10, y + sizeblock - 10), 5)
                pg.draw.line(sc, NASROZOVI, (x + sizeblock - 10, y + 10), (x + 10, y + sizeblock - 10), 5)
            elif color == WHITE_2:
                pg.draw.circle(sc, ORHID, (x + sizeblock // 2, y + sizeblock // 2), sizeblock // 2 - 5, 5)

        if (query - 1) % 2 == 0:
            game_over = check_winners(mas, 'x')
        else:
            game_over = check_winners(mas, 'o')

        if game_over:
            sc.fill(BLACK)
            font = pg.font.SysFont('Calibri', 45)
            text1 = font.render(game_over, True, WHITE, 5)
            text_rect = text1.get_rect()
            text_x = sc.get_width() / 2 - text_rect.width / 2
            text_y = sc.get_height() / 2 - text_rect.height / 2
            sc.blit(text1, [text_x, text_y])

    pg.display.update()
    clock.tick(FPS)
