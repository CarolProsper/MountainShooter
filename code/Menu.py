#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW, C_BLUE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()  # carregando a imagem de fundo do menu
        self.rect = self.surf.get_rect(left=0, top=0)  # criando o retângulo para inserir a imagem


    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')  # Carregando som no menu
        pygame.mixer_music.play(-1)  # com o -1 a música ficará tocando sem parar
        while True:  # loop infinito onde carrega a imagem
            # DESENHAR AS IMAGENS
            self.window.blit(source=self.surf, dest=self.rect)  # vamos desenhar a imagem no retângulo
            self.menu_text(text_size=60, text="Mountain", text_color= C_BLUE, text_center_pos=((WIN_WIDTH / 2), 70))  # escrevendo o nome do jogo
            self.menu_text(text_size=60, text="Shooter", text_color= C_BLUE, text_center_pos=((WIN_WIDTH / 2), 120)) # escrevendo o nome do jogo numa linha abaixo

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=30, text=MENU_OPTION[i], text_color=C_YELLOW, text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))  # criando a cor de seleção do texto no menu
                else:
                    self.menu_text(text_size=30, text=MENU_OPTION[i], text_color=C_WHITE, text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))  # escrevendo o texto do menu
            pygame.display.flip()  # para atualizar a tela

            # CHECAR TODOS OS EVENTOS
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     pygame.quit()  # fecha a janela
                     quit()  # finaliza o jogo
                 if event.type == pygame.KEYDOWN:  # evento de verificação de tecla precionada
                    if event.key == pygame.K_DOWN: # se apertar a tecla seta para baixo... down key
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option +=1  # cresce uma posição
                        else:
                            menu_option = 0  #volta para o início do menu

                    if event.key == pygame.K_UP: # se apertar a tecla seta para cima...  up key
                        if menu_option > 0:
                            menu_option -=1  # diminui uma posição
                        else:
                            menu_option = len(MENU_OPTION) -1  #volta para o tamanho máximo do menu, o final

                    if event.key == pygame.K_RETURN:  # se apertar tecla enter
                        return MENU_OPTION[menu_option]  # retorna para a posição inicial


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):  # Definição do texto.
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
