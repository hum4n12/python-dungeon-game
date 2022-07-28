from abc import ABC, abstractmethod

import pygame


class Drawable(ABC):
    @abstractmethod
    def draw(self, surface: pygame.surface) -> None:
        pass
