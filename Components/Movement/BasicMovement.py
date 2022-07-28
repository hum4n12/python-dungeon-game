from abc import ABC

from pygame.math import Vector2

from Components.Movement.Movable import Movable
from Entity import Entity


class BasicMovement(Movable, ABC):
    def __init__(self, entity: Entity):
        super().__init__(entity)

    def move(self: Movable) -> None:
        if self.offset.length() > 0:
            self.entity.pos += self.offset.normalize() * self.entity.velocity
            # self.offset.x = 0
            # self.offset.y = 0
