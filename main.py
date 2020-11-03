from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import time
import copy

grid = np.array([])


def initialize(size):
    global grid
    grid = np.zeros((size, size), dtype=int)  # 0:


class Ant:
    def __init__(self, grid):
        self.position = np.array([len(grid)//2, len(grid)//2])
        self.direction = np.array([-1, 0])
        self.fig, self.ax = plt.subplots()
        self.img = self.ax.imshow(grid, interpolation="nearest")

    def move(self, frame):
        global grid
        if grid[self.position[0], self.position[1]] == 0:
            # on white cell -> turn clockwise, move forward 1 step
            grid[self.position[0], self.position[1]] = 1
            self.direction[0], self.direction[1] = self.direction[1], - \
                self.direction[0]
        else:
            # on black cell -> turn counter-clockwise, move forward 1 step
            grid[self.position[0], self.position[1]] = 0
            self.direction[0], self.direction[1] = - \
                self.direction[1], self.direction[0]

        self.position += self.direction
        print(grid)
        self.img.set_data(grid)

    def render(self, speed):
        global grid
        self.move(0)
        self.img = self.ax.imshow(grid, interpolation="nearest")
        self.animation = FuncAnimation(
            self.fig, self.move, interval=speed)
        plt.show()


def main():
    size = int(input("Grid size: "))
    speed = int(input("Animation speed: "))
    initialize(size)
    ant = Ant(grid)
    ant.render(speed)


if __name__ == "__main__":
    main()
