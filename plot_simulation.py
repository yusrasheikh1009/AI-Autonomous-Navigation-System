import matplotlib.pyplot as plt
import numpy as np

def plot_navigation(start, goal, path, obstacles):
    plt.figure(figsize=(6, 6))

    # Title
    plt.title("Autonomous Navigation (Agent Moving)", fontsize=14)

    # Black background
    ax = plt.gca()
    ax.set_facecolor("black")

    # Plot obstacles
    for obs in obstacles:
        plt.scatter(obs[0], obs[1], color="white", s=100)

    # Plot path
    if path:
        x_path = [p[0] for p in path]
        y_path = [p[1] for p in path]
        plt.plot(x_path, y_path, color="blue", linewidth=2)

    # Plot start
    plt.scatter(start[0], start[1], color="green", s=100, label="Start")

    # Plot goal
    plt.scatter(goal[0], goal[1], color="red", s=100, label="Goal")

    # Plot agent (current position)
    if path:
        plt.scatter(path[0][0], path[0][1], color="orange", s=100, label="Agent")

    # 🔥 AXIS TICKS (0.0, 2.5, 5.0 ...)
    ticks = np.arange(0, 25, 2.5)
    plt.xticks(ticks)
    plt.yticks(ticks)

    # 🔥 MAKE AXIS VISIBLE ON BLACK BACKGROUND
    plt.tick_params(axis='x', colors='white')
    plt.tick_params(axis='y', colors='white')

    # Labels
    plt.xlabel("X Axis", color="white")
    plt.ylabel("Y Axis", color="white")

    # Grid
    plt.grid(True, color="gray", linestyle="--", linewidth=0.5)

    # Limits
    plt.xlim(0, 25)
    plt.ylim(0, 25)

    # Legend
    legend = plt.legend()
    for text in legend.get_texts():
        text.set_color("black")  # keep legend readable

    plt.show()