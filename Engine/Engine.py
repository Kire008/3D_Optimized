import pygame

class Engine:
    def __init__(self, window):
        self.window = window

        self.mesh_list = []


    def display(self, points):
        self.window.window.fill((0,0,0))

        pygame.draw.circle(self.window.window, (255,0,0), (100,100), 2)

        pygame.display.flip()

    def to_2d_points(self, mesh_verts):
        pass


    def update(self):
        processed_points = self.to_2d_points((100,100))
        self.display(processed_points)