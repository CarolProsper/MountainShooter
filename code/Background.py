#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # velocidade do movimento
        if self.rect.right <= 0:  # qdo o canto direito da imagem de fundo chegar no canto esquerdo
            self.rect.left = WIN_WIDTH  # jogue o canto esquerdo dela no canto direito novamente
            # ... para formar o looping continuo do background.
