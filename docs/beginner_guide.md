# 🎓 Beginner's Guide to Python Prank Tools

> Start here if you're new to Python or this toolkit!

## What is This?

Python Prank Tools is a collection of Python modules that teach you about:
- **System programming** - How to interact with Windows
- **UI manipulation** - Creating visual effects
- **Process management** - How programs run
- **Event handling** - Listening for keyboard/mouse input

## Prerequisites

You need:
1. **Python 3.8+** - Download from [python.org](https://www.python.org/)
2. **A code editor** - VS Code, PyCharm, or any text editor
3. **Windows** - Most examples are Windows-only
4. **Internet** - To install dependencies

## Installation

### Step 1: Install Python

Download Python from [python.org](https://www.python.org/)

During installation, **check "Add Python to PATH"**

### Step 2: Clone the Repository

Open Command Prompt and run:

```bash
git clone https://github.com/pepamatus78-maker/python-prank-tools.git
cd python-prank-tools
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- **pygame** - Graphics and multimedia
- **pillow** - Image manipulation
- **pynput** - Keyboard/mouse control
- **pyautogui** - Screenshot and automation

## Your First Program

### Simple Message Popup

Create a file called `hello_prank.py`:

```python
from modules.message_system import SystemMessenger

# Create a messenger
messenger = SystemMessenger()

# Show a popup
messenger.display_popup("Hello!", "This is my first prank!")
```

Run it:

```bash
python hello_prank.py
```

**Result**: A popup appears on your screen! 🎉

## Understanding the Modules

### 1. Message System

Creates Windows popups and messages.

```python
from modules.message_system import SystemMessenger

messenger = SystemMessenger()

# Simple popup
messenger.display_popup("Title", "Message here")

# Non-blocking (doesn't wait for user to click)
messenger.display_popup_thread("Title", "Quick message")

# Fake UAC dialog
messenger.display_uac_popup()
```

### 2. Keyboard Blocker

Blocks keyboard input temporarily.

```python
from modules.keyboard_blocker import KeyboardDisabler
import time

blocker = KeyboardDisabler()
blocker.start()  # Start blocking

time.sleep(3)   # Block for 3 seconds

blocker.stop()   # Stop blocking
```

⚠️ **WARNING**: If keyboard gets stuck, press `Ctrl+C` multiple times or restart.

### 3. Process Hider

Hides the console window.

```python
from modules.process_hider import ProcessHider

# Hide the console
ProcessHider.hide_console()

# Disguise as another process
ProcessHider.disguise_as("svchost.exe")

# Show console again
ProcessHider.show_console()
```

### 4. Screen Corruptor

Creates glitch effects on images.

```python
from modules.screen_corruptor import ScreenCorruptor
from PIL import Image

# Load an image
img = Image.open("screenshot.png")

# Corrupt it
corruptor = ScreenCorruptor()
corrupted = corruptor.corrupt(img, intensity=0.7)

# Save result
corrupted.save("corrupted.png")
```

## Running Examples

Try these simple examples:

```bash
# Show a popup
python examples/popup_demo.py

# Create glitch effects (if you have an image)
python examples/screen_glitch_demo.py
```

## Common Mistakes

### "ModuleNotFoundError: No module named 'pygame'"

**Solution**: Install requirements

```bash
pip install -r requirements.txt
```

### "pygame.error: no default font"

**Solution**: Pygame couldn't find fonts. This is usually fine, but you can specify a font:

```python
font = pygame.font.SysFont("consolas", 20)
```

### Keyboard won't respond

**Solution**: Press `Ctrl+Alt+Delete` and restart the program, or:

```python
blocker.stop()  # Add this before closing
```

## Learning Path

1. ✅ Run `popup_demo.py` - See what's possible
2. ✅ Read this guide - Understand the concepts
3. ✅ Try simple examples - Modify and experiment
4. ✅ Read module code - See how it works
5. ✅ Build your own - Combine modules
6. ✅ Read advanced guide - Deep dives

## Next Steps

- 📖 Read `docs/advanced_guide.md` for deeper concepts
- 💻 Check `examples/` folder for more demos
- 🔧 Look at module source code to understand
- 🎨 Create your own prank by combining modules

## Getting Help

Stuck? Try:
1. Check the module docstrings: `help(KeyboardDisabler)`
2. Read example code in `examples/` folder
3. Search online for "pynput tutorial" or "pygame tutorial"
4. Open an issue on GitHub

## Important Reminders

⚠️ **ALWAYS**:
- Test on YOUR OWN device first
- Get permission before using on someone else's PC
- Know you can press Ctrl+C to force-quit
- Have backups of important files
- Read DISCLAIMER.md before using

---

Happy pranking! 🎭
