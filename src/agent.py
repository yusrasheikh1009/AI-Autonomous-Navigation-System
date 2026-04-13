from src.planner import astar
import math

class Agent:
    def __init__(self, env):
        self.env = env

        self.start = (2, 2)
        self.goal = (20, 20)

        self.grid_x, self.grid_y = self.start

        # Smooth position
        self.x = self.grid_x + 0.5
        self.y = self.grid_y + 0.5

        self.speed = 0.1

        self.path = []
        self.path_found = False

        self.target_index = 0

    def find_path(self):
        came_from = astar(self.start, self.goal, self.env.obstacles)
        self.reconstruct_path(came_from)
        self.path_found = True

    def reconstruct_path(self, came_from):
        current = self.goal
        self.path = []

        while current != self.start:
            self.path.append(current)
            current = came_from.get(current)

            if current is None:
                print("No path found")
                self.path = []
                return

        self.path.reverse()

    def update(self):
        if not self.path:
            return

        target = self.path[0]
        target_x = target[0] + 0.5
        target_y = target[1] + 0.5

        dx = target_x - self.x
        dy = target_y - self.y

        dist = math.sqrt(dx*dx + dy*dy)

        if dist < 0.05:
            self.path.pop(0)
        else:
            self.x += self.speed * dx
            self.y += self.speed * dy