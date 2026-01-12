import sys
import pygame
pygame.init()

class Window:
    def __init__(self, width=1000, height=800, title="3D Renderer"):
        """
        Initialize settings and window
        """
        self.width = width
        self.height = height
        self.title = title

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        """
        Window info
        """
        self.was_closed = False
        self.was_resized = False

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.