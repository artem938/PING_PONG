import pygame as pg
import sys
import json
from random import randint

WHITE = (255, 255, 255)
LIME = (0, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
YELLOW = (255,255,0)
MAROON = (128,0,0)
BLUE = (0,0,128)

class Base_sprite(pg.sprite.Sprite):
    def __init__(self, pic, x, y, w, h):
        super().__init__()
        self.picture = pg.transform.scale(
            pg.image.load(pic), (w, h)
        ).convert_alpha()
        self.image = self.picture
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.h = h
        
        
        center = self.rect.center
        self.rect.center = center
        self.delta_x = self.rect.x - x 
        self.delta_y = self.rect.y - y

    def draw(self):
        mw.blit(self.picture, (self.rect.x, self.rect.y))

class Racket1(Base_sprite):
    speed = 5

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed 
              
        if keys[pg.K_s] and self.rect.y <= win_y - self.rect.height:            
            self.rect.y += self.speed

class Racket2(Base_sprite):
    speed = 5

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed 
              
        if keys[pg.K_DOWN] and self.rect.y <= win_y - self.rect.height:            
            self.rect.y += self.speed

class Ball(Base_sprite):
    milsec = 0
    sec = 0
    minutes = 0
    points = 0

    speed_x = 0
    speed_y = 0

    def update(self):
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y

        if ball.rect.y <= 0 or ball.rect.y >= 450:
            ball.speed_y *= -1
            ping_ball.play()

        if ball.rect.colliderect(raccket1.rect):
            Ball.points += 1
            ball.speed_y *= +1
            ball.speed_x *= -1
            ping_ball.play()
            
            

        if ball.rect.colliderect(raccket2.rect):
            Ball.points += 1
            ball.speed_y *= +1
            ball.speed_x *= -1
            ping_ball.play()


    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Button:
    def __init__(self, text, x, y, width, height, color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.visible = True

    def draw(self, screen):
        if self.visible:
            pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            font = pg.font.SysFont(None, 40)
            text = font.render(self.text, True, WHITE)
            screen.blit(text, (self.x + (self.width - text.get_width()) // 2, self.y + (self.height - text.get_height()) // 2))

    def is_clicked(self, pos):
        return self.visible and self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height

    def toggle(self):
        self.visible = not self.visible

class Button_mall:
    def __init__(self, text, x, y, width, height, color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.visible = True

    def draw(self, screen):
        if self.visible:
            pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            font = pg.font.SysFont(None, 20)
            text = font.render(self.text, True, WHITE)
            screen.blit(text, (self.x + (self.width - text.get_width()) // 2, self.y + (self.height - text.get_height()) // 2))

    def is_clicked(self, pos):
        return self.visible and self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height

    def toggle(self):
        self.visible = not self.visible


def set_text(screen,text, x, y, color):
    mw.blit(
        font1.render(text, True, color), (x, y)
    )



coins = 0

win_x = 700
win_y = 500

mw = pg.display.set_mode((win_x, win_y))
pg.display.set_caption('TABLE STORM')
background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
clock = pg.time.Clock()


pg.mixer.init()
pg.mixer.music.load('fon_music.ogg')
ping_ball = pg.mixer.Sound('ping_ball.ogg')


button_EXIT = Button('EXIT', 300, 370, 100, 50, RED)
button_play = Button('PlAY', 300, 100, 100, 50, YELLOW)
button_complexity = Button('COMPLEXITY:', 250, 170, 200, 50, LIME)
button_easy = Button('<<EASY>>', 275, 220, 150, 50, GREEN)
button_hard = Button('<<HARD>>', 275, 220, 150, 50, MAROON)
button_control = Button('CONTROL', 275, 295, 150, 50, BLUE)
button_exerise = Button('EXERISE', 40, 170, 150, 50, BLUE)
button_shop = Button('SHOP', 40 , 250 , 150, 50, GREEN)
button_ball1 = Button_mall('ВЫБРАТЬ', 50, 75, 75, 25, BLUE)
button_hard.visible = False




pg.font.init()
font1 = pg.font.Font(None, 36)


ticks = 0


win = False
end = False

play = False

game = True
while game:
    mw.blit(background, (0,0))
    
    if play:
        raccket1.update()
        raccket1.draw()

        raccket2.update()
        raccket2.draw()

        ball.update()
        ball.draw()

        

        Ball.milsec += 1
        if Ball.milsec == 60:
            Ball.milsec = 0
            Ball.sec += 1

        if Ball.sec == 60:
            Ball.milsec = 0
            Ball.sec = 0
            Ball.minutes += 1

     
            
        if Ball.minutes >= 3:
            pg.mixer.music.stop()
            play = False
            end = True
            win = False
            button_EXIT.visible = True
            button_play()

        if ball.rect.x >650:
            play = False
            end = True
            win = False
            button_play.visible = True
            button_EXIT.visible = True
            pg.mixer.music.stop()

        if ball.rect.x <0:
            play = False
            end = True
            win = False
            button_play.visible = True
            button_EXIT.visible = True
            pg.mixer.music.stop()

        if Ball.points == 200:
            play = False
            win = True
            end = False
            button_EXIT.visible = True
            button_play.visible = True
            pg.mixer.music.stop()


        if button_easy.visible == True:
            button_hard.visible = False
            Ball.speed_x = 4
            Ball.speed_y = 4

        if button_hard.visible == True:
            button_easy.visible = False
            Ball.speed_x = 8
            Ball.speed_y = 8

        if Ball.points == 2 and Ball.milsec == 4 and Ball.sec == 4:
            coins += 50

        if Ball.points == 2 and Ball.milsec == 2 and Ball.sec == 2:
            coins += 50

        #if  Ball.minutes == 1 and Ball.milsec == 1 and Ball.points == 26:
            #coins += 100


        if play == True:
            set_text(mw, 'VERSION V1.0', 530, 470, (0,0,0))
        
        
        set_text(mw, f'glasses: {Ball.points}', 60, 50, (0,0,0))
        set_text(mw,f'TIME:{Ball.minutes} minutes {Ball.sec} seconds', 200, 50, (0,0,0))
        set_text(mw, 'VERSION V1.0', 530, 470, (0,0,0))
        set_text(mw, f'COINS{coins}', 30, 450, (0,0,0))
        



    else:
        if win == True:
            set_text(mw,f'you WIN. TIME:{Ball.minutes} minutes {Ball.sec} seconds', 50, 50, (0,0,0))
            set_text(mw, 'VERSION V1.0', 530, 470, (0,0,0))
            set_text(mw, f'COINS{coins}', 30, 450, (0,0,0))
        if end == True:
            set_text(mw,f'you LOSE. TIME:{Ball.minutes} minutes {Ball.sec} seconds', 50, 50, (0,0,0))
            set_text(mw, 'VERSION V1.0', 530, 470, (0,0,0))
            set_text(mw, f'COINS{coins}', 30, 450, (0,0,0))


        button_play.draw(mw)
        button_EXIT.draw(mw)
        button_complexity.draw(mw)
        button_easy.draw(mw)
        button_hard.draw(mw)
        button_control.draw(mw)
        button_exerise.draw(mw)
        button_shop.draw(mw)


        if play == False and win == False and end == False:
            set_text(mw, 'WELCOME TO THE GAME - PING PONG', 130, 20, (100,47,136))
            set_text(mw, 'Press CONTROL or F!', 230, 60, (128,128,128))
            set_text(mw, 'VERSION V1.0', 530, 470, (0,0,0))
            set_text(mw, f'COINS{coins}', 30, 450, (0,0,0))
    
    pg.display.update()

    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
            sys.exit()
        if e.type == pg.MOUSEBUTTONDOWN:
            if button_play.is_clicked(e.pos):
                play = True
                end = False
                ball = Ball('ball_ping.png', randint(100, 400), randint(100, 400), 50, 50)
                raccket1 = Racket1('ping_rocket1.png', 40, 200, 10, 100)
                raccket2 = Racket2('ping_rocket2.png', 640, 200, 10, 100)
                Ball.milsec = 0
                Ball.sec = 0
                Ball.minutes = 0
                Ball.points = 0
                button_EXIT.visible = False
                button_play.visible = False
                pg.mixer.music.play()


        if play == False:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_RETURN:
                    play = True
                    end = False
                    ball = Ball('ball_ping.png', randint(100, 400), randint(100, 400), 50, 50)
                    raccket1 = Racket1('ping_rocket1.png', 40, 200, 10, 100)
                    raccket2 = Racket2('ping_rocket2.png', 640, 200, 10, 100)
                    Ball.milsec = 0
                    Ball.sec = 0
                    Ball.minutes = 0
                    Ball.points = 0
                    button_EXIT.visible = False
                    button_play.visible = False
                    pg.mixer.music.play()

        if e.type == pg.MOUSEBUTTONDOWN:
            if button_easy.is_clicked(e.pos):
                button_easy.toggle()  # Переключаем видимость кнопки 1
                button_hard.toggle()  # Переключаем видимость кнопки 2
            elif button_hard.is_clicked(e.pos):
                button_easy.toggle()  # Переключаем видимость кнопки 1
                button_hard.toggle()  # Переключаем видимость кнопки 2


        if e.type == pg.MOUSEBUTTONDOWN:
            if button_EXIT.is_clicked(e.pos):
                game = False

        if play == False:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    game = False


        elif e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE:
                play = False
                button_play.visible = True
                button_EXIT.visible = True
                button_hard.draw(mw)
                button_easy.draw(mw)
                button_complexity.draw(mw)
                pg.mixer.music.stop()

        if play == False:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    button_easy.toggle()  # Переключаем видимость кнопки 1
                    button_hard.toggle()  # Переключаем видимость кнопки 2
                elif e.key == pg.K_RIGHT:
                    button_easy.toggle()  # Переключаем видимость кнопки 1
                    button_hard.toggle()  # Переключаем видимость кнопки 2

        if e.type == pg.KEYDOWN:
            if e.key == pg.K_f:
                window = pg.display.set_mode((win_x, win_y))
                pg.display.set_caption('TABLE STORM')
                background = pg.transform.scale(pg.image.load('fon4.jpg'), (win_x, win_y))
                clock = pg.time.Clock()

                button_BACK = Button('<-BACK', 25, 420, 150, 50, BLUE)

                game2 = True
                while game2:
                    window.blit(background, (0,0))
                    pg.display.set_caption('CONTROL')
                    set_text(window, 'CONTROL IN MENU:', 25, 25, (255, 255, 255))
                    set_text(window, 'Start the game -- ENTER', 45,50, (255, 255, 255))
                    set_text(window, 'Select difficulty -- < and >', 45, 75, (255, 255, 255))
                    set_text(window, 'Сontrol -- F', 45, 100, (255,255,255))
                    set_text(window, 'Go to the menu or close the game -- ESCAPE', 45, 125, (255,255,255))
                    set_text(window, 'CONTROL IN GAME:', 25, 150, (255,255,255))
                    set_text(window, 'Control the first racket -- W(UP), S(DOWN)', 45, 175, (255,255,255))
                    set_text(window, 'Control the second racket -- UP ,DOWN', 45, 200, (255, 255, 255))
                    set_text(window, 'Press ESCAPE or BACK to exit', 25, 250, (255, 255, 255))
                    set_text(window, 'ATTENTION! the ball falls to the second racket!!!', 25, 300, (255, 255, 255))
                    set_text(window, 'VERSION V1.0', 530, 470, (0,0,0))
                    button_BACK.draw(window)
                    button_BACK.visible = True
                    button_play.visible = False
                    button_EXIT.visible = False
                    button_easy.visible = False
                    button_hard.visible = False
                    button_control.visible = False
                    button_complexity.visible = False

                    for e in pg.event.get():
                        if e.type == pg.QUIT:
                            game2 = False
                            pg.display.set_caption('TABLE STORM')
                            background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
                            clock = pg.time.Clock()
                            button_play.visible = True
                            button_EXIT.visible = True
                            button_easy.visible = True
                            button_hard.visible = False
                            button_control.visible = True
                            button_complexity.visible = True
                            if e.type == pg.KEYDOWN:
                                if e.key == pg.K_LEFT:
                                    button_easy.toggle()  # Переключаем видимость кнопки 1
                                    button_hard.toggle()  # Переключаем видимость кнопки 2
                                elif e.key == pg.K_RIGHT:
                                    button_easy.toggle()  # Переключаем видимость кнопки 1
                                    button_hard.toggle()

                    if e.type == pg.MOUSEBUTTONDOWN:
                        if button_BACK.is_clicked(e.pos):
                            game2 = False
                            pg.display.set_caption('TABLE STORM')
                            background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
                            clock = pg.time.Clock()

                            

                            button_play.visible = True
                            button_EXIT.visible = True
                            button_easy.visible = True
                            button_hard.visible = False
                            button_control.visible = True
                            button_complexity.visible = True
                            if e.type == pg.KEYDOWN:
                                if e.key == pg.K_LEFT:
                                    button_easy.toggle()  # Переключаем видимость кнопки 1
                                    button_hard.toggle()  # Переключаем видимость кнопки 2
                                elif e.key == pg.K_RIGHT:
                                    button_easy.toggle()  # Переключаем видимость кнопки 1
                                    button_hard.toggle()

                    if e.type == pg.KEYDOWN:
                        if e.key == pg.K_ESCAPE:
                            game2 = False
                            pg.display.set_caption('TABLE STORM')
                            background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
                            clock = pg.time.Clock()
                            button_play.visible = True
                            button_EXIT.visible = True
                            button_easy.visible = True
                            button_hard.visible = False
                            button_control.visible = True
                            button_complexity.visible = True
                            if e.type == pg.KEYDOWN:
                                if e.key == pg.K_LEFT:
                                    button_easy.toggle()  # Переключаем видимость кнопки 1
                                    button_hard.toggle()  # Переключаем видимость кнопки 2
                                elif e.key == pg.K_RIGHT:
                                    button_easy.toggle()  # Переключаем видимость кнопки 1
                                    button_hard.toggle()

                    pg.display.update()
                    clock.tick(60)

        
    if e.type == pg.MOUSEBUTTONDOWN:
        if button_control.is_clicked(e.pos):
            window = pg.display.set_mode((win_x, win_y))
            pg.display.set_caption('TABLE STORM')
            background = pg.transform.scale(pg.image.load('fon4.jpg'), (win_x, win_y))
            clock = pg.time.Clock()

            button_BACK = Button('<-BACK', 25, 420, 150, 50, BLUE)

            game2 = True
            while game2:
                window.blit(background, (0,0))
                pg.display.set_caption('CONTROL')
                set_text(window, 'CONTROL IN MENU:', 25, 25, (255, 255, 255))
                set_text(window, 'Start the game -- ENTER', 45,50, (255, 255, 255))
                set_text(window, 'Select difficulty -- < and >', 45, 75, (255, 255, 255))
                set_text(window, 'Сontrol -- F', 45, 100, (255,255,255))
                set_text(window, 'Go to the menu or close the game -- ESCAPE', 45, 125, (255,255,255))
                set_text(window, 'CONTROL IN GAME:', 25, 150, (255,255,255))
                set_text(window, 'Control the first racket -- W(UP), S(DOWN)', 45, 175, (255,255,255))
                set_text(window, 'Control the second racket -- UP ,DOWN', 45, 200, (255, 255, 255))
                set_text(window, 'Press ESCAPE or BACK to exit', 25, 250, (255, 255, 255))
                set_text(window, 'ATTENTION! the ball falls to the second racket!!!', 25, 300, (255, 255, 255))
                set_text(window, 'VERSION V1.0', 530, 470, (0,0,0))
                button_BACK.draw(window)
                button_BACK.visible = True
                button_play.visible = False
                button_EXIT.visible = False
                button_easy.visible = False
                button_hard.visible = False
                button_control.visible = False
                button_complexity.visible = False

                for e in pg.event.get():
                    if e.type == pg.QUIT:
                        game2 = False
                        pg.display.set_caption('TABLE STORM')
                        background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
                        clock = pg.time.Clock()
                        button_play.visible = True
                        button_EXIT.visible = True
                        button_easy.visible = True
                        button_hard.visible = False
                        button_control.visible = True
                        button_complexity.visible = True
                        if e.type == pg.KEYDOWN:
                            if e.key == pg.K_LEFT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()  # Переключаем видимость кнопки 2
                            elif e.key == pg.K_RIGHT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()

                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_ESCAPE:
                        game2 = False
                        pg.display.set_caption('TABLE STORM')
                        background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
                        clock = pg.time.Clock()
                        button_play.visible = True
                        button_EXIT.visible = True
                        button_easy.visible = True
                        button_hard.visible = False
                        button_control.visible = True
                        button_complexity.visible = True
                        if e.type == pg.KEYDOWN:
                            if e.key == pg.K_LEFT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()  # Переключаем видимость кнопки 2
                            elif e.key == pg.K_RIGHT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()

                if e.type == pg.MOUSEBUTTONDOWN:
                    if button_BACK.is_clicked(e.pos):
                        game2 = False
                        pg.display.set_caption('TABLE STORM')
                        background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
                        clock = pg.time.Clock()

                        

                        button_play.visible = True
                        button_EXIT.visible = True
                        button_easy.visible = True
                        button_hard.visible = False
                        button_control.visible = True
                        button_complexity.visible = True
                        if e.type == pg.KEYDOWN:
                            if e.key == pg.K_LEFT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()  # Переключаем видимость кнопки 2
                            elif e.key == pg.K_RIGHT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()


                pg.display.update()
                clock.tick(60)


    if e.type == pg.MOUSEBUTTONDOWN:
        if button_exerise.is_clicked(e.pos):
            m = pg.display.set_mode((win_x, win_y))
            pg.display.set_caption('TABLE STORM')
            background = pg.transform.scale(pg.image.load('black_fon.jpg'), (win_x, win_y))
            clock = pg.time.Clock()

            first_task = False


            button_BACK = Button('<-BACK', 25, 420, 150, 50, BLUE)

            game3 = True
            while game3:
                m.blit(background, (0,0))
                pg.display.set_caption('EXERISE')
                test1 = set_text(m, 'first task: to score 20 points', 25, 25, (255, 255, 255))
                set_text(m, 'VERSION V1.0', 530, 470, (0,0,0))
                button_BACK.draw(m)
                button_BACK.visible = True
                button_play.visible = False
                button_EXIT.visible = False
                button_easy.visible = False
                button_hard.visible = False
                button_control.visible = False
                button_complexity.visible = False


                for e in pg.event.get():
                    if e.type == pg.QUIT:
                        game3 = False
                        pg.display.set_caption('TABLE STORM')
                        background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
                        clock = pg.time.Clock()
                        button_play.visible = True
                        button_EXIT.visible = True
                        button_easy.visible = True
                        button_hard.visible = False
                        button_control.visible = True
                        button_complexity.visible = True
                        if e.type == pg.KEYDOWN:
                            if e.key == pg.K_LEFT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()  # Переключаем видимость кнопки 2
                            elif e.key == pg.K_RIGHT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()

                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_ESCAPE:
                        game3 = False
                        pg.display.set_caption('TABLE STORM')
                        background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
                        clock = pg.time.Clock()
                        button_play.visible = True
                        button_EXIT.visible = True
                        button_easy.visible = True
                        button_hard.visible = False
                        button_control.visible = True
                        button_complexity.visible = True
                        if e.type == pg.KEYDOWN:
                            if e.key == pg.K_LEFT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()  # Переключаем видимость кнопки 2
                            elif e.key == pg.K_RIGHT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()

                if e.type == pg.MOUSEBUTTONDOWN:
                    if button_BACK.is_clicked(e.pos):
                        game3 = False
                        pg.display.set_caption('TABLE STORM')
                        background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
                        clock = pg.time.Clock()

                        

                        button_play.visible = True
                        button_EXIT.visible = True
                        button_easy.visible = True
                        button_hard.visible = False
                        button_control.visible = True
                        button_complexity.visible = True
                        if e.type == pg.KEYDOWN:
                            if e.key == pg.K_LEFT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()  # Переключаем видимость кнопки 2
                            elif e.key == pg.K_RIGHT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()

                if coins > 1:
                    test1 = set_text(m, 'first task: to score 20 points    СДЕЛАНО', 25, 25, (255, 255, 255))

                pg.display.update()
                clock.tick(60)

    if e.type == pg.MOUSEBUTTONDOWN:
        if button_shop.is_clicked(e.pos):
            w = pg.display.set_mode((win_x, win_y))
            pg.display.set_caption('TABLE STORM')
            background = pg.transform.scale(pg.image.load('fon5.png'), (win_x, win_y))
            clock = pg.time.Clock()

            button_BACK = Button('<-BACK', 25, 420, 150, 50, BLUE)

            game4 = True
            while game4:
                w.blit(background, (0,0))
                pg.display.set_caption('SHOP')
                button_BACK.draw(w)
                button_ball1.draw(w)
                button_BACK.visible = True
                button_play.visible = False
                button_EXIT.visible = False
                button_easy.visible = False
                button_hard.visible = False
                button_control.visible = False
                button_complexity.visible = False

                for e in pg.event.get():
                    if e.type == pg.QUIT:
                        game4 = False
                        pg.display.set_caption('TABLE STORM')
                        background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
                        clock = pg.time.Clock()
                        button_play.visible = True
                        button_EXIT.visible = True
                        button_easy.visible = True
                        button_hard.visible = False
                        button_control.visible = True
                        button_complexity.visible = True
                        if e.type == pg.KEYDOWN:
                            if e.key == pg.K_LEFT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()  # Переключаем видимость кнопки 2
                            elif e.key == pg.K_RIGHT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()

                if e.type == pg.MOUSEBUTTONDOWN:
                    if button_ball1.is_clicked(e.pos):
                        ball = Ball('ball2.png', randint(100, 400), randint(100, 400), 50, 50)

                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_ESCAPE:
                        game4 = False
                        pg.display.set_caption('TABLE STORM')
                        background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
                        clock = pg.time.Clock()
                        button_play.visible = True
                        button_EXIT.visible = True
                        button_easy.visible = True
                        button_hard.visible = False
                        button_control.visible = True
                        button_complexity.visible = True
                        if e.type == pg.KEYDOWN:
                            if e.key == pg.K_LEFT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()  # Переключаем видимость кнопки 2
                            elif e.key == pg.K_RIGHT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()

                if e.type == pg.MOUSEBUTTONDOWN:
                    if button_BACK.is_clicked(e.pos):
                        game4 = False
                        pg.display.set_caption('TABLE STORM')
                        background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
                        clock = pg.time.Clock()

                        

                        button_play.visible = True
                        button_EXIT.visible = True
                        button_easy.visible = True
                        button_hard.visible = False
                        button_control.visible = True
                        button_complexity.visible = True
                        if e.type == pg.KEYDOWN:
                            if e.key == pg.K_LEFT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()  # Переключаем видимость кнопки 2
                            elif e.key == pg.K_RIGHT:
                                button_easy.toggle()  # Переключаем видимость кнопки 1
                                button_hard.toggle()


                pg.display.update()
                clock.tick(60)

    clock.tick(60)
