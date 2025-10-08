import random
import matplotlib.pyplot as plt

# ---------------------------
# Agent Class
# ---------------------------
class Agent:
    def __init__(self, id, grid_size, strength=1):
        self.id = id
        self.x = random.randint(0, grid_size - 1)
        self.y = random.randint(0, grid_size - 1)
        self.strength = strength

    def move(self, grid_size):
        # Move randomly in x or y direction (wrap around grid)
        self.x = (self.x + random.choice([-1, 0, 1])) % grid_size
        self.y = (self.y + random.choice([-1, 0, 1])) % grid_size


# ---------------------------
# Competition Simulation (with merging)
# ---------------------------
def competition_simulation(num_agents=20, grid_size=10, steps=30):
    agents = [Agent(i, grid_size) for i in range(num_agents)]
    population_over_time = []
    merge_count = 0

    for step in range(steps):
        # Move all agents
        for agent in agents:
            agent.move(grid_size)

        # Track positions
        positions = {}
        new_agents = []

        for agent in agents:
            pos = (agent.x, agent.y)

            if pos not in positions:
                positions[pos] = agent
                new_agents.append(agent)
            else:
                # MERGE: existing agent and new one combine strength
                existing = positions[pos]
                total_strength = existing.strength + agent.strength
                existing.strength = total_strength
                merge_count += 1  # Count each merge

        agents = new_agents
        population_over_time.append(len(agents))

    print(f"Simulation complete!")
    print(f"Final surviving agents: {len(agents)}")
    print(f"Total merges: {merge_count}")

    return population_over_time


# ---------------------------
# Run Simulation
# ---------------------------
pop_history = competition_simulation(num_agents=20, grid_size=10, steps=30)

# ---------------------------
# Plot Results
# ---------------------------
plt.plot(pop_history, marker='o')
plt.xlabel("Time Steps")
plt.ylabel("Number of Agents")
plt.title("Agent Population Over Time (Merging Rule)")
plt.grid(True)
plt.show()

