from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
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
    # método estático
    def verify_collision(entity_list: list[Entity]):  # parâmetro para verificação de colisão
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod  # método estático
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:  # para cada entidade...
            if ent.health <= 0:  # se a vida for menor ou igual a zero...
                entity_list.remove(ent)  # remove essa entidade da lista.
