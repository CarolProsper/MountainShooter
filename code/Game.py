#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import Menu

import pygame
from pygame import Surface, SurfaceType


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))  # vamos criar nossa janela do jogo

    def run(self):
        while True:
            menu = Menu(self.window)  # vamos chamar nossa tela de Menu
            menu.run()
            pass

            # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # close window
            #         quit()  # end pygame
