#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # velocidade do movimento

    def shoot(self):
        self.shot_delay -= 1  # quando passar nesse laço o delay diminui em 1...
        if self.shot_delay == 0:  # quando o tiro chegar em 0...
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # reset para 30 e atira.
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
