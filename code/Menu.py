#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')  # vamos carregar a imagem de fundo do menu
        self.rect = self.surf.get_rect(left=0, top=0)  # vamos criar o retângulo para inserir a imagem


    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')  # Carregando som no menu
        pygame.mixer_music.play(-1)  # com o -1 a música ficará tocando sem parar sem p
        while True:  # loop infinito onde carrega a imagem
            self.window.blit(source=self.surf, dest=self.rect)  # vamos desenhar a imagem no retângulo
            self.menu_text(text_size=60, text="Mountain", text_color= COLOR_ORANGE, text_center_pos=((WIN_WIDTH/2), 70))  # vamos escrever o texto
            self.menu_text(text_size=60, text="Shooter", text_color= COLOR_ORANGE, text_center_pos=((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=30, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))  # vamos escrever o texto do menu

            pygame.display.flip()  # para atualizar a tela

            # Checando todos os eventos
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     pygame.quit()  # close window
                     quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):  # Definição do texto.
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
