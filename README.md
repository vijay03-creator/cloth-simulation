# 🧵 Cloth Simulation using Pygame

A real-time cloth physics simulation built with Python and Pygame using **Verlet Integration** and **distance constraints**. The cloth behaves like a flexible fabric, responding naturally to gravity and user interaction.

## ✨ Features

* Real-time cloth physics simulation
* Verlet Integration for smooth motion
* Distance constraints between particles
* Gravity-based movement
* Interactive mouse dragging
* Stable cloth behavior using multiple constraint iterations
* Lightweight and beginner-friendly implementation

## 🎮 Demo

Drag the cloth with your mouse and watch it deform naturally while maintaining its structure.

## 🛠️ Technologies Used

* Python 3
* Pygame
* Mathematics (Verlet Integration)
* Physics Simulation Concepts

## 📖 How It Works

The cloth is represented as a grid of particles.

Each particle stores:

* Current Position (x, y)
* Previous Position (old_x, old_y)
* Pinned State

### Verlet Integration

Instead of storing velocity directly, the simulation calculates movement from current and previous positions:

velocity = current_position - previous_position

This provides:

* Smooth motion
* Numerical stability
* Realistic cloth behavior

### Constraints

Particles are connected using distance constraints.

The simulation continuously adjusts particle positions to maintain a fixed spacing, creating the appearance of fabric.

### Interaction

* Left Mouse Button → Drag cloth points
* Top row particles remain pinned
* Gravity pulls the cloth downward

## 🚀 Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/cloth-simulation.git
```

2. Navigate to the project directory

```bash
cd cloth-simulation
```

3. Install dependencies

```bash
pip install pygame
```

4. Run the project

```bash
python cloth.py
```

## 📸 Screenshots

Add screenshots or GIFs here to showcase the simulation.

## 🧠 Concepts Demonstrated

* Physics Simulation
* Game Development
* Computational Mathematics
* Constraint Solving
* Real-Time Rendering
* Interactive Graphics Programming

## 🔮 Future Improvements

* Cloth tearing
* Wind effects
* Collision detection
* Different fabric materials
* GPU acceleration
* Texture rendering

## 👨‍💻 Author

Vijay Maddanimath

B.Tech AIML Student | Python Developer | AI & Software Engineering Enthusiast

If you found this project interesting, consider giving it a ⭐ on GitHub!
