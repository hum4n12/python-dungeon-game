from abc import ABC
from pygame.math import Vector2
from Components.Colliders.Shape import Shape
import pygame


class Circle(Shape, ABC):
    def __init__(self, pos: Vector2, radius: int, offset: Vector2 = Vector2(0, 0)):
        super().__init__(pos, offset)
        self.color = (0, 255, 0)
        self.radius = radius

    def draw(self, surface: pygame.surface) -> None:
        pygame.draw.circle(surface, self.color, self.calculate_pos(), self.radius)

    def collision(self, collider: 'Shape') -> bool:
        return False
