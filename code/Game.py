#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # vamos criar nossa janela do jogo

    def run(self):
        while True:
            menu = Menu(self.window)  # vamos chamar nossa tela de Menu
            menu.run()
            pass

