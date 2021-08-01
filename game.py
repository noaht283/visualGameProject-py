#noah tola nat2eh savannah wilson smw2pd
#game name:MINUTEMEN
# objective of the game is to outlive the countdown while avoiding cannonballs
# can will be shooting projectiles at you from a elevated position while moving, you must dodge in order to not be affected
# projectiles will be able to bounce of walls making it inreasingly harder, more balls as game progresses
# if hit your initial health meter will decrease, once you reach zero you lose and the time recorded is considered your score
import pygame
import gamebox
pygame.init()
camera = gamebox.Camera(800,600)
cannon = gamebox.from_image(400,150,'cannon.png')
x = 0
ground = gamebox.from_color(400,550, 'green',800, 100)
sky = gamebox.from_color(400,0, 'light blue',800, 10)
hpbar1 = gamebox.from_color(70,50, 'green',200, 10)
hpbar2 = gamebox.from_color(730,50, 'green',200, 10)
wall_1 = gamebox.from_color(0,250, 'gray', 50,500)
wall_2 = gamebox.from_color(800,250,'gray',50,500)
hp1 = gamebox.from_text(100,30,'PLAYER 1',50, 'black')
hp2 = gamebox.from_text(700,30,'PLAYER 2',50, 'black')
loser1 = gamebox.from_text(400,300,'PLAYER 2 WINS',100, 'gold')
loser2 = gamebox.from_text(400,300,'PLAYER 1 WINS',100, 'gold')
red = gamebox.from_color(400,300,'red',800,600)
tie = gamebox.from_text(400,300,'TIMES UP',100, 'white')
tie_1 = gamebox.from_text(400,200,'BOTH WINNERS',100, 'white')
start = gamebox.from_color(400,300,'black',800,600)
start_words = gamebox.from_text(400,300,'MINUTEMEN',100, 'white')
herolst = gamebox.load_sprite_sheet('guy.png',4,4)
hero =gamebox.from_image(250,550,herolst[0])
hero_2= gamebox.from_image(550,550,herolst[0])
ball= gamebox.from_circle(400,200,'black',20)
ball2= gamebox.from_circle(400,180,'black',20)
ball3= gamebox.from_circle(400,200,'black',20)
ball4= gamebox.from_circle(400,200,'black',20)
ball5= gamebox.from_circle(400,200,'black',20)
ball6= gamebox.from_circle(400,200,'black',20)
ball7= gamebox.from_circle(400,200,'black',20)
ball8= gamebox.from_circle(400,200,'black',20)
ball9= gamebox.from_circle(400,200,'black',20)
ball10= gamebox.from_circle(400,200,'black',20)
balls = [ball2,ball3,ball4,ball5,ball6,ball7,ball8,ball9,ball10]
timing = 0
timer = 1830
names = gamebox.from_text(400, 30, "Savannah Wilson (smw2pd) and Noah Tola (nat2eh)", 30, "white")
space = gamebox.from_text(400, 60, "Click space to start", 30, "white")
title = gamebox.from_text(400, 300, "MINUTEMEN", 100, "cyan", bold = True)
directions1 = gamebox.from_text(400, 475, "Directions: Players move to avoid the canon's balls for 60 seconds.", 30, "white")
directions2 = gamebox.from_text(400, 500, "Whichever player lasts longer wins.", 30, "white")
directions3 = gamebox.from_text(400, 525, "If the time runs out, both players win.", 30, "white")
directions4 = gamebox.from_text(400, 550, "Player 1 uses the left, right and up keys. Player 2 uses the A, D, and W keys.", 30, "white")

lst = [ground,wall_1,wall_2,ball,ball2,ball3,ball4,ball5,ball6,cannon,hero,hero_2,hp1,hp2,hpbar1,hpbar2]
setting = [ground,wall_1,wall_2]
ball_velocity = 10
ball.xspeed = ball_velocity
ball.yspeed = ball_velocity
ball2.xspeed = ball_velocity
ball2.yspeed = ball_velocity
ball3.xspeed = ball_velocity
ball3.yspeed = ball_velocity
ball4.xspeed = ball_velocity
ball4.yspeed = ball_velocity
ball5.xspeed = ball_velocity
ball5.yspeed = ball_velocity
ball6.xspeed = ball_velocity
ball6.yspeed = ball_velocity
ticks_per_second=30
screen = False

def tick(keys):
    global timing
    global x
    global timer
    global second
    global screen

    if screen == False:
        camera.draw(names)
        camera.draw(title)
        camera.draw(directions1)
        camera.draw(directions2)
        camera.draw(directions3)
        camera.draw(directions4)
        camera.draw(space)
        if pygame.K_SPACE in keys:
            screen=True
    if screen == True:
        timer -= 1
        second = str(int(timer / 30))
        time_box = gamebox.from_text(400, 50, second, 50, 'red')
        camera.clear('blue')
        for i in range(len(lst)):
            camera.draw(lst[i])
            camera.draw(time_box)
        if int(second) < 55:
            ball2.move_speed()
            ball2.move_to_stop_overlapping(ground)
            ball2.move_to_stop_overlapping(wall_1)
            ball2.move_to_stop_overlapping(wall_2)
            ball2.move_to_stop_overlapping(sky)
        if int(second) < 45:
            ball3.move_speed()
            ball3.move_to_stop_overlapping(ground)
            ball3.move_to_stop_overlapping(wall_1)
            ball3.move_to_stop_overlapping(wall_2)
            ball3.move_to_stop_overlapping(sky)
        if int(second) < 35:
            ball4.move_speed()
            ball4.move_to_stop_overlapping(ground)
            ball4.move_to_stop_overlapping(wall_1)
            ball4.move_to_stop_overlapping(wall_2)
            ball4.move_to_stop_overlapping(sky)
        if int(second) < 30:
            ball5.move_speed()
            ball5.move_to_stop_overlapping(ground)
            ball5.move_to_stop_overlapping(wall_1)
            ball5.move_to_stop_overlapping(wall_2)
            ball5.move_to_stop_overlapping(sky)
        if int(second) < 20:
            ball6.move_speed()
            ball6.move_to_stop_overlapping(ground)
            ball6.move_to_stop_overlapping(wall_1)
            ball6.move_to_stop_overlapping(wall_2)
            ball6.move_to_stop_overlapping(sky)


        if pygame.K_UP in keys:
            timing = 3
            while hero_2.y>330:
                hero_2.y -=.05
                hero_2.image = herolst[timing % 16]
        if pygame.K_RIGHT in keys:
            timing = 12
            hero_2.x += 10
            hero_2.y += .05
            hero_2.image = herolst[timing%16]
        if pygame.K_LEFT in keys:
            timing = 11
            hero_2.x -= 10
            hero_2.y += .05
            hero_2.image = herolst[timing % 16]
        if pygame.K_w in keys:
            timing = 3
            while hero.y>330:
                hero.y -=.05
                hero.image = herolst[timing % 16]
        if pygame.K_d in keys:
            timing = 12
            hero.x += 10
            hero.image = herolst[timing%16]
        if pygame.K_a in keys:
            timing = 11
            hero.x -= 10
            hero.image = herolst[timing % 16]
        if hero.bottom > ground.top:
            hero.bottom = ground.top
        if hero.left < wall_1.right:
            hero.left = wall_1.right
        if hero.right > wall_2.left:
            hero.right = wall_2.left
        if hero_2.bottom > ground.top:
            hero_2.bottom = ground.top
        if hero_2.left < wall_1.right:
            hero_2.left = wall_1.right
        if hero_2.right > wall_2.left:
            hero_2.right = wall_2.left
        hero.speedy +=.6
        hero.y += hero.speedy
        hero.move_to_stop_overlapping(ground)
        hero_2.speedy += .6
        hero_2.y += hero_2.speedy
        hero_2.move_to_stop_overlapping(ground)

        ball.move_speed()
        ball.move_to_stop_overlapping(ground)
        ball.move_to_stop_overlapping(wall_1)
        ball.move_to_stop_overlapping(wall_2)
        ball.move_to_stop_overlapping(sky)

        if ball.touches(ground):
            ball.yspeed = -10
        if ball.touches(sky):
            ball.yspeed = 10
        if ball.touches(wall_1):
            ball.xspeed = 10
        if ball.touches(wall_2):
             ball.xspeed = -10
        if ball.touches(hero):
            hpbar1.x -= 5
            if hpbar1.x == 40:
                hpbar1.color = 'yellow'
            if hpbar1.x == 20:
               hpbar1.color = 'red'
        if ball.touches(hero_2):
            hpbar2.x += 5
            if hpbar2.x == 770:
                hpbar2.color = 'yellow'
            if hpbar2.x == 820:
                hpbar2.color = 'red'
        if ball2.touches(ground):
            ball2.yspeed = -10
        if ball2.touches(sky):
            ball2.yspeed = 10
        if ball2.touches(wall_1):
            ball2.xspeed = 10
        if ball2.touches(wall_2):
             ball2.xspeed = -10
        if ball2.touches(hero):
            hpbar1.x -= 5
            if hpbar1.x == 40:
                hpbar1.color = 'yellow'
            if hpbar1.x == 20:
               hpbar1.color = 'red'
        if ball2.touches(hero_2):
            hpbar2.x += 5
            if hpbar2.x == 770:
                hpbar2.color = 'yellow'
            if hpbar2.x == 820:
                hpbar2.color = 'red'
        if ball3.touches(ground):
            ball3.yspeed = -10
        if ball3.touches(sky):
            ball3.yspeed = 10
        if ball3.touches(wall_1):
            ball3.xspeed = 10
        if ball3.touches(wall_2):
             ball3.xspeed = -10
        if ball3.touches(hero):
            hpbar1.x -= 5
            if hpbar1.x == 40:
                hpbar1.color = 'yellow'
            if hpbar1.x == 20:
               hpbar1.color = 'red'
        if ball3.touches(hero_2):
            hpbar2.x += 5
            if hpbar2.x == 770:
                hpbar2.color = 'yellow'
            if hpbar2.x == 820:
                hpbar2.color = 'red'
        if ball4.touches(ground):
            ball4.yspeed = -10
        if ball4.touches(sky):
            ball4.yspeed = 10
        if ball4.touches(wall_1):
            ball4.xspeed = 10
        if ball4.touches(wall_2):
            ball4.xspeed = -10
        if ball4.touches(hero):
            hpbar1.x -= 5
            if hpbar1.x == 40:
                hpbar1.color = 'yellow'
            if hpbar1.x == 20:
                hpbar1.color = 'red'
        if ball4.touches(hero_2):
            hpbar2.x += 5
            if hpbar2.x == 770:
                hpbar2.color = 'yellow'
            if hpbar2.x == 820:
                hpbar2.color = 'red'
        if ball5.touches(ground):
            ball5.yspeed = -10
        if ball5.touches(sky):
            ball5.yspeed = 10
        if ball5.touches(wall_1):
            ball5.xspeed = 10
        if ball5.touches(wall_2):
             ball5.xspeed = -10
        if ball5.touches(hero):
            hpbar1.x -= 5
            if hpbar1.x == 40:
                hpbar1.color = 'yellow'
            if hpbar1.x == 20:
               hpbar1.color = 'red'
        if ball5.touches(hero_2):
            hpbar2.x += 5
            if hpbar2.x == 770:
                hpbar2.color = 'yellow'
            if hpbar2.x == 820:
                hpbar2.color = 'red'
        if ball6.touches(ground):
            ball6.yspeed = -10
        if ball6.touches(sky):
            ball6.yspeed = 10
        if ball6.touches(wall_1):
            ball6.xspeed = 10
        if ball6.touches(wall_2):
             ball6.xspeed = -10
        if ball6.touches(hero):
            hpbar1.x -= 5
            if hpbar1.x == 40:
                hpbar1.color = 'yellow'
            if hpbar1.x == 20:
               hpbar1.color = 'red'
        if ball6.touches(hero_2):
            hpbar2.x += 5
            if hpbar2.x == 770:
                hpbar2.color = 'yellow'
            if hpbar2.x == 820:
                hpbar2.color = 'red'
        if int(second) == 0:
            camera.draw(red)
            camera.draw(tie)
            camera.draw(tie_1)
            gamebox.pause()
        if hpbar1.x == -100:
            camera.draw(loser1)
            gamebox.pause()
        if hpbar2.x == 895:
            camera.draw(loser2)
            gamebox.pause()

    camera.display()
gamebox.timer_loop(30,tick)
