#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Level import Level
from code.Score import Score


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # vamos criar nossa janela do jogo

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)  # vamos chamar nossa tela de Menu
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:  # menu
                player_score = [0, 0]  # lista de score [player1, Player2]
                level = Level(self.window, 'Level1', menu_return, player_score)  # chama o level1 e o score
                level_return = level.run(player_score)  # executa.
                if level_return: # quando encerrar level1...
                    level = Level(self.window, 'Level2', menu_return, player_score)  # chama o level2 e o score
                    level_return = level.run(player_score)  # executa.
                    if level_return:
                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:  # Score
                score.show()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # fecha a janela
                quit()  # finaliza o jogo
            else:
                pass

