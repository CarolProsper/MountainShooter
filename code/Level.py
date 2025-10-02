#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.EntityFactory import EntityFactory
from code.Entity import Entity
from typing import List

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode  # modo de jogo
        self.entity_list: List[Entity] = []  # criou lista vazia
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # gerou lista com os objetos que queria

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # desenha a imagem na tela
                ent.move()
            pygame.display.flip()
        pass
