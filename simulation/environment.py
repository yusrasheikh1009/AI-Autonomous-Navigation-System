import pygame

class Environment:
    def __init__(self):
        pygame.init()

        self.grid_size = 25
        self.cols = 24
        self.rows = 24

        self.width = self.cols * self.grid_size
        self.height = self.rows * self.grid_size

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("AI Autonomous Navigation Simulator")

        self.clock = pygame.time.Clock()
        self.running = True

        self.font = pygame.font.SysFont("Arial", 16)

        # Obstacles (wall-like)
        self.obstacles = [(10, i) for i in range(5, 20)] + [(15, i) for i in range(0, 15)]

    def draw(self):
        # Background
        self.screen.fill((30, 30, 30))

        # Grid
        for x in range(self.cols):
            for y in range(self.rows):
                rect = pygame.Rect(
                    x*self.grid_size,
                    y*self.grid_size,
                    self.grid_size,
                    self.grid_size
                )
                pygame.draw.rect(self.screen, (60, 60, 60), rect, 1)

        # Obstacles
        for obs in self.obstacles:
            pygame.draw.rect(
                self.screen,
                (200, 200, 200),
                (obs[0]*self.grid_size,
                 obs[1]*self.grid_size,
                 self.grid_size,
                 self.grid_size)
            )

    def draw_agent(self, agent):
        x = int(agent.x * self.grid_size)
        y = int(agent.y * self.grid_size)

        pygame.draw.circle(
            self.screen,
            (255, 80, 80),
            (x, y),
            self.grid_size // 2
        )

    def draw_path(self, path):
        for p in path:
            pygame.draw.rect(
                self.screen,
                (100, 255, 100),
                (p[0]*self.grid_size,
                 p[1]*self.grid_size,
                 self.grid_size,
                 self.grid_size)
            )

    def draw_start_goal(self, start, goal):
        # Start (Blue)
        pygame.draw.rect(
            self.screen,
            (80, 80, 255),
            (start[0]*self.grid_size,
             start[1]*self.grid_size,
             self.grid_size,
             self.grid_size)
        )

        # Goal (Purple)
        pygame.draw.rect(
            self.screen,
            (200, 80, 255),
            (goal[0]*self.grid_size,
             goal[1]*self.grid_size,
             self.grid_size,
             self.grid_size)
        )

        # Labels
        self.screen.blit(
            self.font.render("START", True, (255, 255, 255)),
            (start[0]*self.grid_size, start[1]*self.grid_size - 15)
        )

        self.screen.blit(
            self.font.render("GOAL", True, (255, 255, 255)),
            (goal[0]*self.grid_size, goal[1]*self.grid_size - 15)
        )

    def update_display(self):
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def quit(self):
        pygame.quit()