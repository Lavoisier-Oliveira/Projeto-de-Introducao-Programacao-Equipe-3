import pygame
import sys

from parameters import *
from entities.tank import Tank
from entities.flags import Flag
from random import randint

# PyGame Setup
pygame.init()
monitor = pygame.display.Info()  # allow to get current widht and height in any monitor
screen = pygame.display.set_mode((monitor.current_w, monitor.current_h))
pygame.display.set_caption(CAPTION)
background_image = pygame.image.load(R'assets\backgrounds\back2.jpg')  # Load the background image
background_image = pygame.transform.scale(background_image, (monitor.current_w, monitor.current_h))  # Resize the background image to fit the screen
clock = pygame.time.Clock()

p1 = Tank('A', randint(1, 8), [100, 100], 40, 15, KEYS_PLAYER_1)
p2 = Tank('B', randint(1, 8), [200, 200], 50, 11, KEYS_PLAYER_2)
score_p1, score_p2 = 0, 0

# Instanciando a classe Flag 
flag_img = [pygame.image.load('assets/Collectibles/bandeira.png'), pygame.image.load('assets/Collectibles/bandeira_azul.png')] # Imagem da bandeira
size_img = (monitor.current_w//37, monitor.current_h//12)
# Transformando o tamanho da imagem da bandeira
flag_img[0], flag_img[1] = pygame.transform.scale(flag_img[0], (size_img[0], size_img[1])), pygame.transform.scale(flag_img[1], (size_img[0], size_img[1])) 
flag = Flag((monitor.current_w, monitor.current_h), flag_img[0], size_img) # Classe Flag instanciada 
flag_cycle, del_flag_time, flag_p, flag_taken = 1, 1, False, False # Variavéis para fazer a checagem das condições da bandeira na tela

game_is_running = True
while game_is_running:
	font = pygame.font.Font(None, 48)
	game_time = pygame.time.get_ticks()
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  # para sair, pressione o X da janela ou ESC
			game_is_running = False
	
	screen.blit(background_image, (0, 0))  # Desenhar o background

	# Atualizar o estado do tanque
	for player in Tank.tanks:
		player.update()

	score_tab1 = font.render(f': {score_p1}', True, (0, 0, 0))
	screen.blit(flag_img[0], (monitor.current_w*0.01, background_image.get_height()*0.9))
	screen.blit(score_tab1, (background_image.get_width()*0.036, background_image.get_height()*0.93))
	score_tab2 = font.render(f': {score_p2}', True, (0, 0, 0))
	screen.blit(flag_img[1], (monitor.current_w*0.904, background_image.get_height()*0.9))
	screen.blit(score_tab2, (background_image.get_width()*0.93, background_image.get_height()*0.93))

	# Gerando uma bandeira em um local aleatório no intervalo de 7 segundos
	if game_time > 7000*flag_cycle and game_time < 10000*flag_cycle:
		flag.render(screen) # Função da classe Flag para renderizar a flag em um local aleatório
		flag_cycle += 1
		flag_p, flag_taken = True, False
	# Após 3 segundos que a bandeira foi gerada, ela não deve mais aparecer na tela
	if game_time > 10000*del_flag_time: 
		flag_p = False
		del_flag_time += 1
	if flag_p:
		flag.update(screen)	# Função para sempre renderizar a bandeira na tela
	
	if p1.rect.colliderect(flag.rect_self(flag_p)):
		print(1)
		# if not flag_taken:
		# 	score_p1 += 1
		# flag_p, flag_taken = False, True
	elif p2.rect.colliderect(flag.rect_self(flag_p)):
		if not flag_taken:
			score_p2 += 1
		flag_p, flag_taken = False, True

	# Renderizar o jogo
	# screen.fill("black")  # Preencher a tela com uma cor (preto)
	for player in Tank.tanks:
		screen.blit(player.image, player.rect.topleft)  # Desenhar o tanque na nova posição

	# Flip the display to put your work on screen
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
sys.exit()
