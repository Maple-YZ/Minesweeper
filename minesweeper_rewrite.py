import pygame
import sys
import os


class Clickable():
    def __init__(self, border: tuple[int], ) -> None:
        self.border = border
        self.clicked = False
    
    def press_on(self):
        self.clicked = True
        
    def release_on(self):
        self.clicked = False


class Plot(Clickable):
    def __init__(self, border: tuple[int]) -> None:
        super().__init__(border)


class Game():

    def __init__(self, window_size = (375, 375), ) -> None:
        self._window_size = window_size
        self.resouce = dict()
    
    def init_window(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(self._window_size)
        pygame.display.set_caption("minesweeperV1.0")
        pygame.display.set_icon(self.resouce["boom"])
    
    def load_resource(self) -> None:
        for file in os.listdir('resource'):
            if file.endswith('.png'):
                self.resouce[file[:-4]] = pygame.image.load(f'resource/{file}')

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
    game.load_resource()
    game.init_window()
    game.run()