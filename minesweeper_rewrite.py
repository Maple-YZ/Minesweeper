import pygame
import sys

class Game():

    def __init__(self, window_size = (375, 375), ) -> None:
        self._window_size = window_size
        self.screen = pygame.display.set_mode(self._window_size)

    def config(self, window_size=None):
        if window_size:
            self._window_size = window_size
            self.screen

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()

    def draw(self, slot, draw_type):
        self.screen.blit(draw_type, self.slot_to_pos(slot))

    @staticmethod
    def slot_to_pos(slot: tuple[int]) -> tuple[int]:
        return ((slot[0] + 3) * 25, (slot[1] + 3) * 25)

    @staticmethod
    def pos_to_slot(self, pos: tuple[int]) -> tuple[int]:
        return (pos[0] // 25 - 3, pos[1] // 25 - 3)

if __name__ == "__main__":
    game = Game()
    game.run()