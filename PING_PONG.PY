import pygame as pg

import sys

from random import randint

WHITE = (255, 255, 255)
LIME = (0, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
YELLOW = (255,255,0)
MAROON = (128,0,0)

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





def set_text(text, x, y, color=(0,0,0)):
    mw.blit(
        font1.render(text, True, color), (x, y)
    )



win_x = 700
win_y = 500


mw = pg.display.set_mode((win_x, win_y))
pg.display.set_caption('настольный шторм')
background = pg.transform.scale(pg.image.load('fon2.jpg'), (win_x, win_y))
clock = pg.time.Clock()

fon_win = pg.image.load("fon_win.png")
fon_win = pg.transform.scale(fon_win, (win_x, win_y))

fon_end = pg.image.load("fon_end.png")
fon_end = pg.transform.scale(fon_end, (win_x, win_y))

pg.mixer.init()
pg.mixer.music.load('fon_music.ogg')
ping_ball = pg.mixer.Sound('ping_ball.ogg')


button_EXIT = Button('EXIT', 300, 370, 100, 50, RED)
button_play = Button('PlAY', 300, 150, 100, 50, YELLOW)
button_complexity = Button('COMPLEXITY', 250, 220, 200, 50, LIME)
button_easy = Button('EASY', 300, 270, 100, 50, GREEN)
button_hard = Button('HARD', 300, 270, 100, 50, MAROON)
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

        if Ball.points == 20:
            play = False
            win = True
            end = False
            button_EXIT.visible = True
            button_play.visible = True
            pg.mixer.music.stop()

        if button_easy.visible == True:
            Ball.speed_x = 4
            Ball.speed_y = 4

        if button_hard.visible == True:
            Ball.speed_x = 6
            Ball.speed_y = 6

        
        set_text(f'Очки: {Ball.points}', 60, 50)
        set_text(f'Время:{Ball.minutes} Минут {Ball.sec} секунды', 200, 50)


    else:
        if win == True:
            set_text(f'ВЫ ВЫЙГРАЛИ. ВРЕМЯ:{Ball.minutes} минут {Ball.sec} секунды', 50, 50)
        if end == True:
            set_text(f'ВЫ ПРОИГРАЛИ. ВРЕМЯ:{Ball.minutes} минут {Ball.sec} секунды', 50, 50)


        button_play.draw(mw)
        button_EXIT.draw(mw)
        button_complexity.draw(mw)
        button_easy.draw(mw)
        button_hard.draw(mw)



    
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
                Ball.milsec
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




    clock.tick(60)