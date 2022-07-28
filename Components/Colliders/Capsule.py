from abc import ABC
from pygame.math import Vector2

from Components.Colliders.Circle import Circle
from Components.Colliders.Rectangle import Rectangle
from Components.Colliders.Shape import Shape
import pygame


class Capsule(Shape, ABC):
    def __init__(self, pos: Vector2, width: int, height: int):
        super().__init__(pos)
        self.width = width
        self.height = height
        self.radius = int(width / 2)
        # height - width because circle radius is half of a width, so two circles give us offset height of width length
        self.rectangle = Rectangle(self.pos, width, height - width, Vector2(0, self.radius))
        self.upperCircle = Circle(self.pos, self.radius, Vector2(self.radius, self.radius))
        self.bottomCircle = Circle(self.pos, self.radius, Vector2(self.radius, self.height - self.radius))

    def draw(self, surface: pygame.surface) -> None:
        self.upperCircle.draw(surface)
        self.bottomCircle.draw(surface)
        self.rectangle.draw(surface)

    def collision(self, collider: 'Shape') -> bool:
        return False
