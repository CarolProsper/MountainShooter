#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # atraso do tiro, para sair tiro em sequência

    def move(self, ):  # movimento do jogador
        pressed_key = pygame.key.get_pressed()  # quando a tecla estiver pressionada algo acontece:
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:  # pressionar seta para cima, até topo
            self.rect.centery -= ENTITY_SPEED[self.name]  # vai subir
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT: # pressionar seta baixo, até base
            self.rect.centery += ENTITY_SPEED[self.name]  # vai descer
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # pressionar seta para esquerda, até a base
            self.rect.centerx -= ENTITY_SPEED[self.name]  # vai para esquerda
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH: # pressionar seta direita, até base
            self.rect.centerx += ENTITY_SPEED[self.name]  # vai para direita
        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:  # quando o tiro chegar em 0...
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # reset para 100 ...
            pressed_key = pygame.key.get_pressed()  # e atira.
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
