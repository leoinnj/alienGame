import pygame.font

class Scoreboard():
    def __init__(self,ai_settings,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_img = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.screen.blit(self.score_img,self.screen_rect)



