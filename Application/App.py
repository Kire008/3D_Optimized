from Application.Window import Window
from Application.Input import Input
from Engine.Engine import Engine

class Application:
    def __init__(self):
        self.window = Window()
        self.engine = Engine(self.window)
        self.input = Input(self.window)


    def run(self):
        while not self.window.was_closed:
            self.window.update()
            self.input.update()
            self.engine.update()