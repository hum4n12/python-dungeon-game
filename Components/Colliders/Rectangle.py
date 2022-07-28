from abc import ABC
from pygame.math import Vector2
from Components.Colliders.Shape import Shape
import pygame


class Rectangle(Shape, ABC):
    def __init__(self, pos: Vector2, width: int, height: int, offset: Vector2 = Vector2(0, 0)):
        super().__init__(pos, offset)
        self.width = width
        self.height = height

    def draw(self, surface: pygame.surface) -> None:
        pos = self.calculate_pos()
        pygame.draw.rect(surface, self.color, pygame.Rect(pos.x, pos.y, self.width, self.height))

    def collision(self, collider: 'Shape') -> bool:
        return False
