import pygame
from parameters import *

class HomeMenuScreen:
    def __init__(self):
        self.start_game = False
        self.start_button = pygame.Rect((SCREEN_WIDTH // 2) - 100, SCREEN_HEIGHT // 2, 200,50) # configurando o botão de início
        self.background_image = pygame.image.load("assets/backgrounds/home_background.png")
        self.background_image = pygame.transform.scale(self.background_image, SCREEN_SIZE)

        # texto do botão
        self.font = pygame.font.Font(None, 36)
        self.button_text = self.font.render("Iniciar",True, (0,0,0))


    def handle_event(self, event):  # detectar se clicou no botão de início
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.start_button.collidepoint(x,y):
                self.start_game = True


    def draw (self, screen):
        screen.blit(self.background_image, (0,0)) # desenha a imagem de fundo
        pygame.draw.rect(screen, (255,0,0), self.start_button) # cria o botão de início
        
        # desenha o texto do botão
        text_rect = self.button_text.get_rect(center=self.start_button.center)
        screen.blit(self.button_text, text_rect)

        # coloca "CinEXPLODA" no centro da tela
        title_font = pygame.font.Font(None,74)
        title_text = title_font.render("Cinflito de Tanques",True, (255,255,255))
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(title_text, title_rect)