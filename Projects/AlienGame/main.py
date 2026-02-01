import pygame
import sys
import random


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("AlienGame")
        self.background_color = (214,222,11)
        self.Nave = Nave(self.screen)
        self.Alien = Alien(self.screen)
        self.y_proj = 770
        self.move = False
        self.y_alien = 0
        self.vel_alien = 0.09
        self.lifes = 3
        self.kills=0
        self.font = pygame.font.SysFont(None, 36)


    def run_game(self,):
        
        while True:
            
            if self.y_proj<0:
                self.move = False
                self.y_proj = self.screen.get_height() - 30

            for event in pygame.event.get(): 
                
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.move = True
                

            
            self.screen.fill(self.background_color)
            self.nave_rect = self.Nave.desenhar_nave()
            

            ###CONTADOR DE KILLS AND CONTADOR DE VIDAS
            pygame.draw.rect(self.screen,(0,0,255),(self.screen.get_width()-300,0,300,40),width=0)
            self.Kills_count = self.font.render(f"KILLS:{self.kills}", True, (255, 255, 255))
            self.screen.blit(self.Kills_count, (self.screen.get_width()-100, 0))

            self.lifes_count = self.font.render(f"LIFES:{self.lifes}", True, (255, 255, 255))
            self.screen.blit(self.lifes_count, (self.screen.get_width()-250, 0))

            
            ####--------------- 


            ###NIVES-----
            if self.kills <=3:
                self.Alien.numero_aliens = random.randint(0,3)
                self.vel_alien = 0.09
            elif self.kills >=4 and self.kills <=7:
                self.vel_alien = 0.09*1.3
                self.Alien.numero_aliens =  random.randint(4,7)
            elif self.kills >7 :
                self.vel_alien = 0.09*1.5
                self.Alien.numero_aliens =  random.randint(7,20)


            ###----------



            if self.move: 
                self.projetil_rect = self.Nave.projeteis(y=self.y_proj) 
                self.y_proj-=1


                
                for i,alien_rect in enumerate(self.Alien.aliens):
                        if self.projetil_rect:
                            if self.projetil_rect.colliderect(alien_rect):
                                del self.Alien.aliens[i]
                                self.kills+=1
                                if len(self.Alien.aliens) ==0:
                                    self.y_alien=0


            
            
            if self.lifes>0:
                
                self.y_alien +=self.vel_alien 
                if self.y_alien<= self.screen.get_height():
                    self.Alien.draw_aliens(y=self.y_alien) 

                else: 
                    self.Alien.aliens.clear()
                    self.y_alien = 0


                for i,Alien in enumerate(self.Alien.aliens):     
                    if Alien.colliderect(self.nave_rect):
                        del self.Alien.aliens[i]
                        self.y_alien=0
                        self.lifes-=1
            
            
            pygame.display.flip()


class Nave:
    def __init__(self,screen):
        """"Class Que define as Funcoes da Nave"""
        self.screen = screen
        self.nave_width = 30
        self.nave_heigth = 30
        self.color_nave = (0,0,0)
        self.color_projetil = (255,0,0)
        self.vel = 1
        self.x = self.screen.get_width()//2
        self.y = self.screen.get_height() - self.nave_heigth
        self.x_proj = self.x
        
    
    def desenhar_nave(self,):
        
        keys = pygame.key.get_pressed()   
        if keys[pygame.K_d]:
           self.x +=self.vel
        if keys[pygame.K_a]:
            self.x-=self.vel

        
        """
        if keys[pygame.K_w]:
            self.y-=self.vel
        if keys[pygame.K_s]:
            self.y+=self.vel
        """
        if self.x >= (self.screen.get_width()-self.nave_width):
            self.x = self.screen.get_width()-self.nave_width

        if self.x <= 0:
            self.x = 0
        """
        if self.y <= 0:
            self.y = 0
        if self.y >= self.screen.get_height()-self.nave_heigth:

            self.y = self.screen.get_height()-self.nave_heigth
        """
        return pygame.draw.rect(self.screen,self.color_nave,pygame.Rect(self.x,self.y,self.nave_width,self.nave_heigth),width=0)

    def projeteis(self,y):
        

        self.y_proj = y
        self.vel_proj = 2
        self.proj_width = 10
        self.proj_height  = 10
        
        if self.y_proj == self.y:
            
            self.x_proj = self.x

        return pygame.draw.rect(self.screen,self.color_projetil,pygame.Rect(self.x_proj + self.proj_width//2,self.y_proj,self.proj_width,self.proj_height),width=0)

class Alien:


    def __init__(self,screen):
        self.screen = screen
        self.x_alien = 0
        self.numero_aliens = 1
        self.aliens = list()
        self.color_alien = (255,0,0)
        
        self.build_alien()

    def build_alien(self,):
        for n in range(self.numero_aliens):
            self.aliens.append(pygame.Rect(random.randint(0,self.screen.get_width() - 20) ,0,35,35))
        
    
    def draw_aliens(self,y):

        if len(self.aliens)>0:
            for  alien in self.aliens:
                alien.y=y
                pygame.draw.rect(self.screen,self.color_alien,alien)
            
        else:
            self.build_alien()
        

game = Game()
game.run_game()