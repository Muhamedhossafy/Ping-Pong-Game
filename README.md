# 🏓 **Ping Pong Game** 

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Game](https://img.shields.io/badge/Genre-Arcade%20Sports-green)
![License](https://img.shields.io/badge/License-MIT-orange)

## 🎮 **Game Overview**
A classic Ping Pong arcade game built with Python's Turtle graphics, featuring realistic physics, dual-player controls, and competitive scoring.

## ✨ **Key Features**
- 🕹️ **Dual-player controls** (W/S and Arrow Keys)
- ⚡ **Dynamic ball physics** with speed acceleration
- 📊 **Score tracking** with first-to-7 win condition
- 🎨 **Clean visual design** with Turtle graphics
- � **Authentic paddle mechanics** with precise collision

## 🛠️ **Technical Implementation**

### 🏓 **Game Components**
```python
# Core Game Structure
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
```

### 🎯 **Class Architecture**
1. **Paddle Class** - Player-controlled paddles
2. **Ball Class** - Game ball with physics
3. **Scoreboard Class** - Score tracking and display

## 📦 **System Requirements**
- Python 3.8+
- Turtle module (standard library)

## ⚙️ **Installation**
```bash
git clone https://github.com/yourusername/ping-pong-game.git
cd ping-pong-game
```

## 🚀 **How to Run**
```bash
python ping_pong.py
```

## 🎮 **Game Controls**
| Player | Controls |
|--------|----------|
| Left Player | W (Up), S (Down) |
| Right Player | ↑ (Up), ↓ (Down) |

## 📊 **Scoring System**
- First player to reach 7 points wins
- Ball resets after each point
- Progressive speed increase

## 🖥️ **Game Interface Preview**
```
    Left: 3   |   Right: 5
    -------------------------
    |                       |
    |   |               |   |
    |   |       ○       |   |
    |   |               |   |
    |                       |
    -------------------------
```

## 📂 **Project Structure**
```
ping-pong/
├── ping_pong.py       # Main game file
├── paddle.py          # Paddle implementation
├── ball.py            # Ball physics
├── scoreboard.py      # Scoring system
└── README.md          # Documentation
```

## 🤝 **Contributing Guidelines**
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## 📜 **License**
MIT License - See [LICENSE](LICENSE) for details

## 📧 Contact
- ✉️ **Email**: [muhamedammar0900@gmail.com](mailto:muhamedammar0900@gmail.com)  
- 🔗 **LinkedIn**: [Muhamad Ammar](https://www.linkedin.com/in/muhamad-ammar-18b427306)
  
---

**Happy gaming!** For bug reports or feature requests, please open an issue on GitHub.

## 🏆 **Victory Condition**
First player to score 7 points wins the match with a dramatic "GAME OVER" screen!
