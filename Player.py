import pygame
from abc import ABC

from Components.Colliders.Capsule import Capsule
from Components.Colliders.Circle import Circle
from Components.Colliders.Rectangle import Rectangle
from Components.Drawable import Drawable
from Components.Movement.BasicMovement import BasicMovement
from Components.Movement.Movable import Movable
from Entity import Entity
from pygame.math import Vector2

PLAYER_VELOCITY = 10


class Player(Entity, Drawable, ABC):
    def __init__(self, pos: Vector2) -> None:
        super().__init__(pos, PLAYER_VELOCITY)
        self.movable_component: Movable = BasicMovement(self)
        self.rect = Rectangle(pos, 50, 60)
        # self.shape = Circle(pos, 50)
        self.shape = Capsule(pos, 50, 80)

    def update(self, dt: int) -> None:
        self.movable_component.move()

    def draw(self, surface: pygame.surface) -> None:
        self.shape.draw(surface)
        # self.rect.draw(surface)

    def keyboard_handler(self, event: pygame.event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.movable_component.offset.y = -1
            elif event.key == pygame.K_s:
                self.movable_component.offset.y = 1
            elif event.key == pygame.K_a:
                self.movable_component.offset.x = -1
            elif event.key == pygame.K_d:
                self.movable_component.offset.x = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                if pygame.key.get_pressed()[pygame.K_s]:
                    self.movable_component.offset.y = 1
                else:
                    self.movable_component.offset.y = 0
            elif event.key == pygame.K_s:
                if pygame.key.get_pressed()[pygame.K_w]:
                    self.movable_component.offset.y = -1
                else:
                    self.movable_component.offset.y = 0
            elif event.key == pygame.K_a:
                if pygame.key.get_pressed()[pygame.K_d]:
                    self.movable_component.offset.x = 1
                else:
                    self.movable_component.offset.x = 0
            elif event.key == pygame.K_d:
                if pygame.key.get_pressed()[pygame.K_a]:
                    self.movable_component.offset.x = -1
                else:
                    self.movable_component.offset.x = 0
