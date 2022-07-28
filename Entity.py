import pygame
from abc import ABC, abstractmethod

from Components.Colliders.Shape import Shape


class Entity(ABC):
    def __init__(self, pos: pygame.math.Vector2, velocity: float = 0, shape: Shape = None) -> None:
        self.pos = pos
        self.velocity = velocity
        self.shape = shape

    @abstractmethod
    def update(self, dt: int) -> None:
        pass
