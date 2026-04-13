from simulation.environment import Environment
from src.agent import Agent
from plot_simulation import plot_navigation
import time

def main():
    env = Environment()
    agent = Agent(env)

    plotted = False

    while env.running:
        env.clock.tick(60)

        # Handle events
        env.handle_events()

        # Draw background + grid + obstacles
        env.draw()

        # Find path once
        if not agent.path_found:
            agent.find_path()

        # Plot graph once
        if agent.path_found and not plotted:
            plot_navigation(
                agent.start,
                agent.goal,
                agent.path.copy(),
                env.obstacles
            )
            plotted = True

        # Update movement
        agent.update()

        # Draw visuals
        env.draw_path(agent.path)
        env.draw_start_goal(agent.start, agent.goal)
        env.draw_agent(agent)

        # 🔥 IMPORTANT: update display AFTER drawing everything
        env.update_display()

        time.sleep(0.02)

    env.quit()


if __name__ == "__main__":
    main()