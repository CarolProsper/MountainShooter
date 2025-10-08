#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player

import random


class EntityFactory:

    @staticmethod  # método estático
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':    # fizemos o background do Level1
                list_bg = []    # fizemos o movimento do Parallax
                for i in range(7):  # laço referente numero de imagens do level 1
                    # 7 imagens aparecem no inicio da tela
                    list_bg.append(Background(f'Level1Bg{i}', position := (0, 0)))
                    # as mesmas 7 imagens aparecem no fim da tela
                    list_bg.append(Background(f'Level1Bg{i}', position := (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':    # fizemos o background do Level1
                list_bg = []    # fizemos o movimento do Parallax
                for i in range(5):  # laço referente numero de imagens do level 2
                    # 7 imagens aparecem no inicio da tela
                    list_bg.append(Background(f'Level2Bg{i}', position := (0, 0)))
                    # as mesmas 7 imagens aparecem no fim da tela
                    list_bg.append(Background(f'Level2Bg{i}', position := (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
