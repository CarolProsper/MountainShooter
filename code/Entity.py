#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame


class Entity(ABC):  # classe abstrata
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()  # carrega a imagem.
        # Extensão convert_alpha trabalha de maneira otimizada o arquivo png.
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # faz o retângulo
        self.speed = 0

    @abstractmethod  # decorator
    def move(self, ):
        pass
