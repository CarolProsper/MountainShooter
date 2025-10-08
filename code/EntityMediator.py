from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    # __ significa que esse método é privado, só é invocado aqui dentro.
    def __verify_collision_window(ent: Entity):  # parâmetro para verificação se atingiu limite da tela
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:  # quando o inimigo sumir no canto direito da tela...
                ent.health = 0  # a vida dela zera e ele é destruído.
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:  # quando o tiro sumir no canto esquerdo da tela...
                ent.health = 0  # a vida dela zera e ele é destruído.
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:  # quando o tiro sumir no canto direito da tela...
                ent.health = 0  # a vida dela zera e ele é destruído.

    @staticmethod
    def __verify_collision_entity(ent1, ent2):  # parâmetro para verificação de colisão entre entidades
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:  # if valid_interaction == True.
            # se a borda direita de E1 está à direita da borda esquerda de E2 e
            # se a borda esquerda de E1 está à esquerda da borda direita de E2 e
            # se a borda inferior de E1 está abaixo da borda superior de E2 e
            # se a borda superior de E1 está acima da borda inferior de E2:
            # se todas forem True, haverá colisão!
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage  # a vida do ent1 vai diminuir ao dano causado pela ent2.
                ent2.health -= ent1.damage  # a vida do ent2 vai diminuir ao dano causado pela ent1.
                ent1.last_dmg = ent2.name  # o último dano em e1 foi causado por e2.
                ent2.last_dmg = ent1.name  # o último dano em e2 foi causado por e1.

    @staticmethod
    # método estático
    def __give_score(enemy: Enemy, entity_list: list[Entity]):  # método para score
        if enemy.last_dmg == 'Player1Shot':  # se o último dano no inimigo foi dado pelo tiro do Player1
            for ent in entity_list:  # vai varrer a lista de entidades:
                if ent.name == 'Player1':  # e vai procurar esse player1.
                    ent.score += enemy.score  # o escore da entidade recebe o score do inimigo.
        elif enemy.last_dmg == 'Player2Shot':  # se o último dano no inimigo foi dado pelo tiro do Player2
            for ent in entity_list:  # vai varrer a lista de entidades:
                if ent.name == 'Player2':  # e vai procurar esse player2.
                    ent.score += enemy.score  # o escore da entidade recebe o score do inimigo.

    @staticmethod
    # método estático
    def verify_collision(entity_list: list[Entity]):  # parâmetro para verificação de colisão
        for i in range(len(entity_list)):  # laço repetição, pega uma entidade por vez.
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i+1, len(entity_list)):  # compara cada entidade com todas as outras entidades
                #  usa-se i+1 para não haver redundância na comparação, comparações repetidas,
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    # método estático
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:  # para cada entidade...
            if ent.health <= 0:  # se a vida for menor ou igual a zero...
                if isinstance(ent, Enemy):  # se for um Inimigo:
                    EntityMediator.__give_score(ent, entity_list)
                    # passa a entidade como parâmetro e a lista para saber quem foi morto e quem matou, e chama o score,
                entity_list.remove(ent)  # remove essa entidade da lista (mata).
