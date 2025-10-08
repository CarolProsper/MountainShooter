#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import pygame

from pygame import Surface, Rect
from pygame.font import Font
from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.Entity import Entity
from typing import List

from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode  # modo de jogo
        self.entity_list: List[Entity] = []  # criou lista vazia
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # gerou lista com os objetos que queria
        self.entity_list.append(EntityFactory.get_entity('Player1'))  # inicializou jogador 1
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))  # inicializa o jogador 2
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME) # A CADA DETERMINADO TEMPO, VAMOS CRIAR UM INIMIGO

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')  # importando a música
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()  # garante que essa função rode sempre num tempo específico.
        while True:
            clock.tick(60)  # Define quantos fps vai usar. Quanto maior, mais rapido vai executar.
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # desenha a imagem na tela
                ent.move()
                if isinstance(ent, (Player, Enemy)):  # se minha entidade for um desses dois...
                    shoot = ent.shoot()
                    if shoot is not None:  # se existir um tiro
                        self.entity_list.append(shoot)  # vai puxar o shot para dentro da lista de entidades.
                if ent.name == 'Player1':  # se houver Player 1:
                    self.level_text(14, f'Player1 - Health:  {ent.health} | Score: {ent.score}', C_GREEN,
                                    (10, 25))
                if ent.name == 'Player2':  # se houver Player 2:
                    self.level_text(14, f'Player2 - Health:  {ent.health} | Score: {ent.score}', C_CYAN,
                                    (10, 45))
            for event in pygame.event.get():  # gerenciador de evento para fechar a janela no level 1
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', "Enemy2"))  # vai criar inimigos aleatoriamente
                    self.entity_list.append(EntityFactory.get_entity(choice))  # e inicializa o inimigo

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE,
                            (10, 5))  # mostra o tempo de duração da fase
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE,
                            (10, WIN_HEIGHT - 35))  # imprime, em tempo real, o fps na tela.
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE,
                            (10, WIN_HEIGHT - 20))  # mostra quantas entidades têm na tela
            pygame.display.flip()
            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)  # verifica colisão
            EntityMediator.verify_health(entity_list=self.entity_list)  # verifica as vidas
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
