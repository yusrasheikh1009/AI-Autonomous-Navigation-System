# 🚗 AI-Based Autonomous Navigation System

---

## 📌 Overview

This project is an AI-based autonomous navigation system designed to simulate how intelligent agents navigate from a start point to a goal while avoiding obstacles.

It mimics real-world systems used in self-driving cars, warehouse robots, and delivery bots by combining path planning, environment simulation, and visualization.

---

## 🚀 Key Features

* 🤖 Autonomous agent navigation using A* algorithm
* 🧠 Intelligent path planning (shortest path)
* 🧱 Obstacle avoidance system
* 🎮 Real-time simulation using Pygame
* 📊 Graph-based visualization using Matplotlib
* 📍 Start & Goal position tracking
* 📈 Axis-based movement visualization (0.0, 2.5, etc.)

---

## 🔄 System Workflow

Start Position → Environment Mapping → Path Planning (A*) → Obstacle Avoidance → Agent Movement → Goal Reached

---

## 🧠 Tech Stack

| Category        | Tools Used       |
| --------------- | ---------------- |
| Programming     | Python           |
| Simulation      | Pygame           |
| Visualization   | Matplotlib       |
| Algorithms      | A* Path Planning |
| Data Handling   | NumPy            |
| Version Control | Git & GitHub     |

---

## 🤖 System Details

**Algorithm:** A* (A-Star Pathfinding)

**Input:**

* Grid-based environment
* Start position
* Goal position
* Obstacles

**Process:**

* Grid creation
* Heuristic-based path search
* Shortest path computation

**Output:**

* Optimal path from start to goal
* Real-time agent movement
* Visual graph representation

---

## 📊 Output

* 🟦 Start Position
* 🟪 Goal Position
* 🟩 Computed Path
* 🔴 Moving Agent
* ⚪ Obstacles
* 📈 Graph visualization with axis values

---

## 🖥️ Run the Project

### ▶️ Run Simulation

python main.py

### 📊 Graph Output

* Automatically opens after path calculation

---

## 📁 Project Structure

AI-Autonomous-Navigation-System/
│
├── simulation/
│   └── environment.py
│
├── src/
│   ├── agent.py
│   ├── planner.py
│   └── utils.py
│
├── plot_simulation.py
├── main.py
├── requirements.txt
├── README.md
│
├── images/
│   ├── simulation.png
│   ├── graph.png
│
├── videos/

---

## 📸 Results

### 🎮 Simulation Output

<img src="images/simulation.png" width="600"/>

### 📊 Graph Visualization

<img src="images/graph.png" width="600"/>

---

## 🎯 Conclusion

This project demonstrates how AI-based systems can autonomously navigate environments using intelligent path planning and obstacle avoidance.

It showcases:

* AI-based decision making
* Algorithmic path planning
* Simulation-based testing
* Visualization for analysis

---

## 🚀 Future Improvements

* Real-time obstacle detection
* Integration with ROS
* 3D simulation using advanced tools
* Reinforcement Learning-based navigation
* Multi-agent systems
* Drone navigation simulation

---

## 👩‍💻 Author

**Yusra Sheikh Ashfaq**

---

⭐ If you like this project, give it a star!

