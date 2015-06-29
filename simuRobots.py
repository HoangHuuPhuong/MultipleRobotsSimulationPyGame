#/user/bin/env python
#### Written by Phuong H. Hoang, November 2014
import sys
import pygame
from pygame import time


###created modules by PHUONG HOANG###
path_module = '/home/phuong/phuonghoang/created_module'
sys.path.append(path_module)

from pygame_setup import cl_pygame_setup
from math_function import cl_math_function

class cl_simu_mr(object):
    
    def __init__(self):
        self.pygame = cl_pygame_setup()
        self.math = cl_math_function()
        self.display_mode = (800, 600)
        self.caption  = 'multiple robots'
        self.color = self.pygame.get_color() #white, black, red, green,blue, yellow, cyan, purple
        self.count_steps = 0
        self.angle_unit = 3
        self.traj_steps = 0

    def moving_single_robot(self):
        game_display = self.pygame.display_game(self.display_mode, self.caption)
        game_exit = False
        lead_x = 300
        lead_y = 300
        while not game_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        lead_x -= 10
                    if event.key == pygame.K_RIGHT:
                        lead_x += 10
            game_display.fill(self.color[0])
            pygame.draw.rect(game_display, self.color[3], [lead_x, lead_y,10,10])
            pygame.display.update()
        pygame.quit()
        quit()

    
    def plan_hardcoded(self):
        [r1,  r2, r3, r4] = [[50, 100],[50,120], [750, 100], [750, 120]]
        payload = [55,95]
        game_display = self.pygame.display_game(self.display_mode, self.caption)
        game_exit = False
        while not game_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:                          
                        r1[0] -= 10 
                        r2[0] -= 10
                        r3[0] += 10
                        r4[0] += 10
                        payload[0] -= 10
                    if event.key == pygame.K_RIGHT:
                        r1[0] += 10 
                        r2[0] += 10
                        r3[0] -= 10
                        r4[0] -= 10
                        payload[0] += 10
            game_display.fill(self.color[0])
            pygame.draw.rect(game_display, self.color[3], [r1[0], r1[1],20,10])
            pygame.draw.rect(game_display, self.color[3], [r2[0], r2[1],20,10])
            pygame.draw.rect(game_display, self.color[1], [r3[0], r3[1],20,10])
            pygame.draw.rect(game_display, self.color[1], [r4[0], r4[1],20,10])
            pygame.draw.rect(game_display, self.color[2], [payload[0], payload[1],10,40])

            pygame.display.update()
        pygame.quit()
        quit()

    def plan_mr(self):
        [r1,  r2, r3, r4] = [[50, 100],[50,130], [750, 100], [750, 130]]
        payload = [43,80] 
        game_display = self.pygame.display_game(self.display_mode, self.caption)
        game_exit = False
        while not game_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
            if self.count_steps < 250:
                r1[0] +=1
                r2[0] +=1
                r3[0] -=1
                r4[0] -=1
                payload[0] +=1
                self.count_steps +=1 
            
            if self.count_steps == 250:
                r1 = [r1[0], r1[1]]
                r2 = [r2[0], r2[1]]
                p_center = self.math.find_center(r1, r2)
                #print p_center
                traj_r1 = self.math.plan_circular_trajectory(r1, p_center, self.angle_unit)
                traj_r2 = self.math.plan_circular_trajectory(r2, p_center, self.angle_unit)
                self.count_steps +=1
            if ((self.count_steps > 250) and (self.traj_steps < 18)):
                r1 = traj_r1[self.traj_steps]
                r2 = traj_r2[self.traj_steps]
                r3[0] -=1
                r4[0] -=1
                payload[0] +=1
                self.count_steps +=1
                self.traj_steps +=1

            if ( (self.traj_steps >= 18) and (self.traj_steps < 400) ):
                r1[1] +=1
                r2[1] +=1
                r3[0] -=1
                r4[0] -=1
                payload[0] +=1
                self.count_steps +=1
                self.traj_steps +=1
                
            game_display.fill(self.color[0])
            pygame.draw.circle(game_display, self.color[3], r1,12)
            pygame.draw.circle(game_display, self.color[3], r2,12)
            pygame.draw.circle(game_display, self.color[1], r3,12)
            pygame.draw.circle(game_display, self.color[1], r4,12)
            pygame.draw.rect(game_display, self.color[2], [payload[0], payload[1],14,70])
            

            pygame.display.update()
            time.wait(50)          
        pygame.quit()
        quit()

    def plan_mr_cir(self):
        [r1,  r2, r3, r4] = [[50, 95],[50,135], [750, 100], [750, 130]]
        payload = [50,115]
        font = pygame.font.SysFont("Times New Roman, Arial", 20)
        text = font.render("Multiple Robot Simulation - UNIST", True, self.color[7])
        turtle_img = pygame.image.load('turtlebot.jpeg')
        turtle_img = pygame.transform.scale(turtle_img, (100, 60))
        stuff1_img = pygame.image.load('stuff1.jpeg')
        stuff1_img = pygame.transform.scale(stuff1_img, (287, 400))
        stuff2_img = pygame.image.load('stuff2.jpeg')
        stuff2_img = pygame.transform.scale(stuff2_img, (320, 400))
        game_display = self.pygame.display_game(self.display_mode, self.caption)
        game_exit = False
        while not game_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
            if self.count_steps < 90:
                r1[0] +=3
                r2[0] +=3
                r3[0] -=3
                r4[0] -=3
                payload[0] +=3
                self.count_steps +=1 
            
            if self.count_steps == 90:
                r1 = [r1[0], r1[1]]
                r2 = [r2[0], r2[1]]
                p_center = self.math.find_center(r1, r2)
                #print p_center
                traj_r1 = self.math.plan_circular_trajectory(r1, p_center, self.angle_unit)
                #print traj_r1
                traj_r2 = self.math.plan_circular_trajectory(r2, p_center, self.angle_unit)
                #print traj_r2
                traj_payload = self.math.plan_circular_trajectory(payload, p_center, self.angle_unit)
                self.count_steps +=1
            if ((self.count_steps > 90) and (self.traj_steps < 30)):
                r1 = traj_r1[self.traj_steps]
                r2 = traj_r2[self.traj_steps]
                r3[0] -=1
                r4[0] -=1
                payload = traj_payload[self.traj_steps]
                self.count_steps +=1
                self.traj_steps +=1

            if ( (self.traj_steps >= 30) and (self.traj_steps < 150) ):
                r1[1] +=3
                r2[1] +=3
                r3[0] -=3
                r4[0] -=3
                payload[1] +=3
                self.count_steps +=1
                self.traj_steps +=1
                
            game_display.fill(self.color[0])
            
            pygame.draw.rect(game_display, self.color[5], [10, 75,790,5])
            pygame.draw.rect(game_display, self.color[5], [10, 150,282,5])
            pygame.draw.rect(game_display, self.color[5], [460, 150,440,5])
            pygame.draw.rect(game_display, self.color[6], [287, 155,5,450])
            pygame.draw.rect(game_display, self.color[6], [460, 155,5,450])
            pygame.draw.rect(game_display, self.color[4], [370, 195,5,50])
            pygame.draw.rect(game_display, self.color[4], [370, 295,5,50])
            pygame.draw.rect(game_display, self.color[4], [370, 395,5,50])
            pygame.draw.rect(game_display, self.color[4], [370, 495,5,50])

            pygame.draw.circle(game_display, self.color[3], r1,12)
            pygame.draw.circle(game_display, self.color[3], r2,12)
            pygame.draw.circle(game_display, self.color[1], r3,12)
            pygame.draw.circle(game_display, self.color[1], r4,12)
            pygame.draw.circle(game_display, self.color[2], payload,25)
            game_display.blit(text, (10,10))
            game_display.blit(turtle_img, (700, 0))
            game_display.blit(stuff1_img, (0, 155))
            game_display.blit(stuff2_img, (465, 155))
            pygame.display.update()
            time.wait(100)          
        pygame.quit()
        quit()

    def plan_mr_img(self):
        [r1,  r2, r3, r4] = [[50, 95],[50,135], [750, 100], [750, 130]]
        payload = [30,95]
        payload_img = pygame.image.load('payload.jpg')
        payload_img = pygame.transform.scale(payload_img, (45, 40))
        game_display = self.pygame.display_game(self.display_mode, self.caption)
        game_exit = False
        while not game_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
            if self.count_steps < 90:
                r1[0] +=3
                r2[0] +=3
                r3[0] -=3
                r4[0] -=3
                payload[0] +=3
                self.count_steps +=1 
            
            if self.count_steps == 90:
                r1 = [r1[0], r1[1]]
                r2 = [r2[0], r2[1]]
                p_center = self.math.find_center(r1, r2)
                #print p_center
                traj_r1 = self.math.plan_circular_trajectory(r1, p_center, self.angle_unit)
                traj_r2 = self.math.plan_circular_trajectory(r2, p_center, self.angle_unit)
                traj_payload = self.math.plan_circular_trajectory(payload, p_center, self.angle_unit)
                self.count_steps +=1
            if ((self.count_steps > 90) and (self.traj_steps < 30)):
                r1 = traj_r1[self.traj_steps]
                r2 = traj_r2[self.traj_steps]
                r3[0] -=1
                r4[0] -=1
                payload = traj_payload[self.traj_steps]
                self.count_steps +=1
                self.traj_steps +=1

            if ( (self.traj_steps >= 30) and (self.traj_steps < 150) ):
                r1[1] +=3
                r2[1] +=3
                r3[0] -=3
                r4[0] -=3
                payload[1] +=3
                self.count_steps +=1
                self.traj_steps +=1
            payload_tuple = (payload[0], payload[1])
            game_display.fill(self.color[0])
            pygame.draw.circle(game_display, self.color[3], r1,12)
            pygame.draw.circle(game_display, self.color[3], r2,12)
            pygame.draw.circle(game_display, self.color[1], r3,12)
            pygame.draw.circle(game_display, self.color[1], r4,12)
            game_display.blit(payload_img, payload_tuple)
            #pygame.draw.circle(game_display, self.color[2], payload,25)

            pygame.display.update()
            time.wait(100)          
        pygame.quit()
        quit()
        
    
def main():

    plan_mr = cl_simu_mr()
    #plan_mr.moving_single_robot()
    plan_mr.plan_mr_cir()
    #plan_mr.plan_mr_img()
    

if __name__ == "__main__":
    main()
