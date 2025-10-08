#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import pygame

from pygame import Surface, Rect
from pygame.font import Font
from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.Entity import Entity
from typing import List

from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: List[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode  # modo de jogo
        self.entity_list: List[Entity] = []  # criou lista vazia
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))  # gerou lista com os objetos que queria
        player = (EntityFactory.get_entity('Player1'))  # inicializou jogador1
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = (EntityFactory.get_entity('Player2'))  # inicializou jogador2
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME) # A CADA DETERMINADO TEMPO, VAMOS CRIAR UM INIMIGO
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP) # A CADA 100 MS VAI CHECAR A CONDIÇÃO DE VITORIA

    def run(self, player_score: List[int]):
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
                if event.type == pygame.QUIT:  # checa se está fechando a janela
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:  # checa se dá para fazer um spaw no inimigo
                    choice = random.choice(('Enemy1', "Enemy2"))  # vai criar inimigos aleatoriamente
                    self.entity_list.append(EntityFactory.get_entity(choice))  # e inicializa o inimigo
                if event.type == EVENT_TIMEOUT:  # checa se o timeout está acontecendo.
                    self.timeout -= TIMEOUT_STEP  # vai decrementando o tempo
                    if self.timeout == 0:  # até encerrar.
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':  # se existir um player e for o player1...
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':  # se existir um player e for o player2...
                                player_score[0] = ent.score
                        return True

                found_player = False  # condição se jogador morrer
                for ent in self.entity_list: # varre a lista de entidades
                    if isinstance(ent, Player): # verifica se existe o player
                        found_player = True  # se encontrar fica true

                if not found_player:  # se não encontrar (morreu)
                    return False  # retorna falso.

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE,
                            (10, 5))  # mostra o tempo de duração da fase em segundos com 2 casas decimais: /1000:.1f}s.
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE,
                            (10, WIN_HEIGHT - 35))  # imprime, em tempo real, o fps na tela.
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE,
                            (10, WIN_HEIGHT - 20))  # mostra quantas entidades têm na tela
            pygame.display.flip()
            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)  # verifica colisão
            EntityMediator.verify_health(entity_list=self.entity_list)  # verifica as vidas

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
