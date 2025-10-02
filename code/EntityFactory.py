#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod  # método estático
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':    # fizemos o background do Level1
                list_bg = []    # fizemos o movimento do Parallax
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', position := (0, 0)))  # 7 imagens aparecem no inicio da tela
                    list_bg.append(Background(f'Level1Bg{i}', position := (WIN_WIDTH, 0)))  # as mesmas 7 imagens aparecem no fim da tela
                return list_bg
