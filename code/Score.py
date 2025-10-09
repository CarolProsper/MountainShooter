import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_YELLOW, SCORE_POS, C_BLUE, MENU_OPTION, C_WHITE, C_RED
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()  # carregando a imagem de fundo do menu
        self.rect = self.surf.get_rect(left=0, top=0)  # criando o retângulo para inserir a imagem

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')  # Carregando som no score
        pygame.mixer_music.play(-1)  # com o -1 a música ficará tocando sem parar
        db_proxy = DBProxy('DBScore')  # quando quiser salvar algum dado, conecta com o BD
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(60, 'YOU WIN!', C_BLUE, SCORE_POS['Title'])
            text = 'Enter Player 1 name (máx 5 characters):'
            score = player_score[0]
            if game_mode == MENU_OPTION[0]:  # 1 player
                score = player_score[0]
            if game_mode == MENU_OPTION[1]:  # cooperativo
                score = (player_score[0] + player_score[1]) / 2  # média da soma das duas pontuações
                text = 'Enter Team name (máx 5 characters):'
            if game_mode == MENU_OPTION[2]:  # competitivo
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name (máx 5 characters):'
            self.score_text(35, text, C_RED, SCORE_POS['EnterName'])

            for event in pygame.event.get():  # gerenciador de evento para fechar a janela no score
                if event.type == pygame.QUIT:  # checa se está fechando a janela
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 5:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:  # se a tecla apertada for backspace
                        name = name[:-1]  # apaga o último caractere
                    else:
                        if len(name) < 5:
                            name += event.unicode
            self.score_text(35, name, C_YELLOW, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self,):
        pygame.mixer_music.load('./asset/Score.mp3')  # Carregando som no score
        pygame.mixer_music.play(-1)  # com o -1 a música ficará tocando sem parar
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_BLUE, SCORE_POS['Title'])
        self.score_text(20, ' NAME            SCORE                  DATE        ', C_WHITE, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')  # acessar o BD
        list_score = db_proxy.retrieve_top10()  # puxar o score
        db_proxy.close()  # fecha a conexão com o BD

        # laço de repetição para imprimir linha por linha o top 10
        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'[{name}            {score :05d}             {date}', C_YELLOW, SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():  # gerenciador de evento para fechar a janela no score
                if event.type == pygame.QUIT:  # checa se está fechando a janela
                    pygame.quit()
                    sys.exit()
                if event. type == KEYDOWN:   # esc para voltar a tela principal
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()  # atualiza a tela toda vez
            pass

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):  # Definição do texto.
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
