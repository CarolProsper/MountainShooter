from code.Enemy import Enemy
from code.Entity import Entity


class EntityMediator:

    @staticmethod
    # __ significa que esse método é privado, só é invocado aqui dentro.
    def __verify_collision_window(ent: Entity):  # parâmetro para verificação se atingiu limite da tela
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:  # quando a entidade sumir no canto direito da tela...
                ent.health = 0  # a vida dela zera.
        pass

    @staticmethod  # método estático
    def verify_collision(entity_list: list[Entity]):  # parâmetro para verificação de colisão
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod  # método estático
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:  # para cada entidade...
            if ent.health <= 0:  # se a vida for menor ou igual a zero...
                entity_list.remove(ent)  # remove essa entidade da lista.
