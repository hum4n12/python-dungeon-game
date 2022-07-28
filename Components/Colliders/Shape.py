from abc import ABC, abstractmethod

import pygame
from pygame.math import Vector2

from Components.Drawable import Drawable


class Shape(Drawable, ABC):
    def __init__(self, pos: Vector2, offset: Vector2 = Vector2(0, 0)):
        self.pos = pos
        self.color = (255, 0, 0)
        self.offset = offset

    @abstractmethod
    def collision(self, collider: 'Shape') -> bool:
        pass

    @abstractmethod
    def draw(self, surface: pygame.surface) -> None:
        pass

    def calculate_pos(self) -> Vector2:
        return Vector2(self.pos.x + self.offset.x, self.pos.y + self.offset.y)

    def set_color(self, color: tuple[int, int, int]) -> None:
        self.color = color
