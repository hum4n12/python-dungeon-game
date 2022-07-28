import pygame
import sys
from Player import Player


class Main:
    clock = pygame.time.Clock()
    WINDOW_SIZE = (1200, 720)
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    player: Player = Player(pygame.math.Vector2(100, 100))

    @staticmethod
    def setup() -> None:
        pygame.init()
        pygame.display.set_caption('My Pygame Window')

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))

        self.player.draw(self.screen)

        pygame.display.update()

    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.player.keyboard_handler(event)

        self.player.update(100)

    def main(self) -> None:
        Main.setup()

        while True:
            self.update()
            self.draw()
            self.clock.tick(60)


main = Main()
main.main()
