import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        # initial ship's original position
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # locate ship at screen center and bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # enable ship center position in float
        self.center = float(self.rect.centerx)

        # moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # update ship's center value but rect
        # screen   top,left,bottom,right
        if self.moving_right and self.rect.right < self.screen_rect.width:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)