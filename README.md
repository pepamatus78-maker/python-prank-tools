# 🎭 Python Prank Tools - Educational Toolkit

> **⚠️ DISCLAIMER**: This toolkit is for **EDUCATIONAL PURPOSES ONLY**. Use only on devices you own or have explicit permission to use. Unauthorized use may violate computer fraud laws.

A comprehensive Python toolkit for creating harmless pranks and educational demonstrations. Learn about system manipulation, UI effects, and more!

## 📚 What's Included

### Core Modules
- **keyboard_blocker.py** - Block keyboard input
- **screen_corruptor.py** - Create glitch/corruption effects
- **process_hider.py** - Hide console windows and disguise processes
- **file_manager.py** - Safe file operations with recovery options
- **message_system.py** - Create system message popups
- **desktop_manager.py** - Virtual desktop manipulation

### Example Scripts
- **salinewin.exe.py** - Complete prank simulation (the corn virus)
- **simple_keyboard_block.py** - Basic keyboard blocking demo
- **screen_glitch_demo.py** - Screen effect showcase
- **popup_demo.py** - Message system examples

### Documentation
- **DISCLAIMER.md** - Legal warnings
- **docs/beginner_guide.md** - For Python newcomers
- **docs/advanced_guide.md** - Deep dives into each module
- **docs/examples.md** - Copy-paste ready examples

## 🚀 Quick Start

### Installation

```bash
# Clone the repo
git clone https://github.com/pepamatus78-maker/python-prank-tools.git
cd python-prank-tools

# Install dependencies
pip install -r requirements.txt
```

### Run a Demo

```bash
# Simple popup demo (safe!)
python examples/popup_demo.py

# Screen glitch demo
python examples/screen_glitch_demo.py

# Full prank (with music file)
python examples/salinewin.exe.py
```

## 📖 Learning Path

1. **Start here**: `docs/beginner_guide.md`
2. **Try demos**: Run examples in `examples/` folder
3. **Read modules**: Check `modules/` for detailed code
4. **Build your own**: Combine modules to create new pranks

## 🎯 Module Overview

### keyboard_blocker.py
```python
from modules.keyboard_blocker import KeyboardDisabler

blocker = KeyboardDisabler()
blocker.start()  # Block all keyboard input
# ... do stuff ...
blocker.stop()   # Re-enable keyboard
```

### screen_corruptor.py
```python
from modules.screen_corruptor import ScreenCorruptor

corruptor = ScreenCorruptor()
corrupted_image = corruptor.corrupt(image, intensity=0.5)
```

### message_system.py
```python
from modules.message_system import SystemMessenger

messenger = SystemMessenger()
messenger.display_popup("Title", "Message content")
```

## 📋 Requirements

- Python 3.8+
- pygame
- pillow
- pynput
- pyautogui

See `requirements.txt` for full list.

## 🤝 Contributing

Found a bug? Have a cool prank idea? Submit a pull request or open an issue!

## ⚖️ Legal Notice

**DO NOT use this toolkit to:**
- Access systems without permission
- Damage or destroy data maliciously
- Disrupt business operations
- Create actual malware
- Violate any laws

**DO use this toolkit to:**
- Learn about system programming
- Create pranks on your own devices
- Educate others about security
- Participate in authorized security testing

## 📞 Support

- Check `docs/` for detailed guides
- See `examples/` for working code
- Read module docstrings for API docs
- Open an issue on GitHub

## 📄 License

MIT License - See LICENSE file

---

**Remember**: With great code comes great responsibility! 🦸‍♂️