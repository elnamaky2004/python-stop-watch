# PyQt5 Stopwatch

A lightweight **Stopwatch desktop app** built with **PyQt5**.  
It supports **Start / Stop / Reset** and displays time in **mm:ss.cc** (centiseconds), updating every **10ms** using `QTimer`.

## Preview
- Time format: `MM:SS.CC`
- Update interval: `10ms` (0.01s)
- Buttons:
  - **Start** → begins counting
  - **Stop** → pauses counting
  - **Reset** → resets time back to `00:00.00`

## Features
- ✅ Simple, clean PyQt5 UI (QVBoxLayout + QHBoxLayout)
- ✅ Accurate ticking using `QTimer`
- ✅ Centisecond display (milliseconds / 10)
- ✅ Button state handling (disables Start while running)

## Tech Stack
- Python 3
- PyQt5 (`QWidget`, `QLabel`, `QPushButton`, `QTimer`, `QTime`)

## Installation

### 1) Clone the repo
```bash
git clone https://github.com/<your-username>/pyqt5-stopwatch.git
cd pyqt5-stopwatch
