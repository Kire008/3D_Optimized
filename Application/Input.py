import pygame

class Input:
    def __init__(self, window):
        self.window = window

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            self.window.close()