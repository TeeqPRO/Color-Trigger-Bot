# 🎯 Color Trigger Bot

A minimal, color-based trigger bot that automatically clicks when a pixel color change is detected near your cursor.  
Runs in the background with a simple GUI showing monitoring status.

## 🧠 How It Works

The bot checks the colors of two pixels (left and right of the cursor at `x-2` and `x+2`).  
If either color changes, it triggers a mouse click and stops monitoring.

## 🎮 Controls

- `F6` — start monitoring
- `ESC` — manually stop monitoring

## 💻 GUI

- Displays current status (ON/OFF)
- Green — monitoring active
- Red — monitoring inactive

## ▶️ Getting Started

Install dependencies:
```bash
pip install pyautogui keyboard
```

Run the script:
```bash
python main.py
```

Or download the precompiled `.exe` (for Windows):  
👉 [Releases](https://github.com/TeeqPRO/Color-Trigger-Bot/releases/)

> No Python installation needed for the `.exe` version.

## 📁 Files

- `main.py` — main script with logic and GUI
- `.exe` — optional compiled version (in Releases)
