from abc import ABC, abstractmethod
from Entity import Entity
from pygame.math import Vector2


class Movable(ABC):
    def __init__(self, entity: Entity):
        self.offset = Vector2(0, 0)
        self.entity = entity

    @abstractmethod
    def move(self: Entity) -> None:
        pass
