import sys
import pygame
from Log.log import Log

pygame.init()


class Window:
    def __init__(self, width=1000, height=800, title="3D Renderer"):
        """
        Initialize settings and window
        """
        self.width = width
        self.height = height
        self.title = title

        self.window = pygame.display.set_mode(
            (self.width, self.height),
            pygame.RESIZABLE
        )
        pygame.display.set_caption(self.title)

        self.log = Log()
        self.log.clear_all_logs()


        """
        Window info
        """
        self.was_closed     = False
        self.was_resized    = False

    def close(self):
        self.was_closed = True
        """Log info"""
        self.log.log(f"\nWindow closed     {self.was_closed}")

        # Close
        pygame.quit()
        sys.exit()

    def update(self):
        self.was_resized = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()

            # Check for Resize
            if event.type == pygame.VIDEORESIZE:
                self.was_resized = True
                self.width      = event.size[0]
                self.height     = event.size[1]
                self.window     = pygame.display.set_mode((
                    self.width, self.height),
                    pygame.RESIZABLE
                )


                # Start Log
                self.log.log(
f"""
Window resized:
Width:          {self.width}
Height:         {self.height}
""")
                # Stop Log