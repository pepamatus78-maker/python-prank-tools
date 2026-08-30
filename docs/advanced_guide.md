# 🚀 Advanced Guide - Deep Dives

> For developers who want to understand the internals and build custom pranks.

## Architecture Overview

```
python-prank-tools/
├── modules/              # Core functionality
│   ├── keyboard_blocker.py
│   ├── screen_corruptor.py
│   ├── process_hider.py
│   ├── message_system.py
│   └── __init__.py
├── examples/             # Usage examples
│   ├── popup_demo.py
│   ├── screen_glitch_demo.py
│   └── salinewin.exe.py
├── docs/                 # Documentation
│   ├── beginner_guide.md
│   ├── advanced_guide.md
│   └── examples.md
└── requirements.txt      # Dependencies
```

## How Keyboard Blocking Works

### The pynput Library

`pynput` intercepts keyboard events at the OS level.

```python
from pynput import keyboard

def on_press(key):
    try:
        print(f"Key: {key.char}")
    except AttributeError:
        print(f"Special Key: {key}")
    
    # Return False to block the key
    return False  # This blocks it!

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # Keep listening
```

### Threading

Keyboard blocking runs in a daemon thread so it doesn't block your main program:

```python
def run_listener():
    with keyboard.Listener(...) as listener:
        listener.join()

thread = threading.Thread(target=run_listener, daemon=True)
thread.start()
```

### Stopping the Listener

```python
listener.stop()  # Safely stop listening
```

## Screen Corruption Effects

### RGB Channel Separation

Separates the Red, Green, Blue channels and shifts them:

```python
r, g, b = image.split()  # Get RGB channels

# Shift red channel to the right
r = r.transform((w, h), Image.AFFINE, (1, 0, 10, 0, 1, 0))

# Shift blue channel to the left
b = b.transform((w, h), Image.AFFINE, (1, 0, -10, 0, 1, 0))

# Merge back together
image = Image.merge("RGB", (r, g, b))
```

### Screen Tearing

Takes horizontal strips and shifts them randomly:

```python
# Extract a horizontal strip
strip = image.crop((0, y, width, y + height))

# Paste it at a different X position
image.paste(strip, (offset_x, y))
```

### Affine Transforms

Pillow's `Image.transform()` uses affine matrices:

```python
# (a, b, c, d, e, f) represents:
# x' = a*x + b*y + c
# y' = d*x + e*y + f

# Shift right by 10:
(1, 0, 10, 0, 1, 0)

# Rotate 45 degrees:
(0.707, -0.707, 0, 0.707, 0.707, 0)
```

## Process Hiding

### Windows API Calls

Using `ctypes` to call Windows API:

```python
import ctypes

# Get console window handle
hwnd = ctypes.windll.kernel32.GetConsoleWindow()

# Hide window (SW_HIDE = 0)
ctypes.windll.user32.ShowWindow(hwnd, 0)

# Move off-screen
ctypes.windll.user32.SetWindowPos(hwnd, 0, -999, -999, 1, 1, 0x0001)
```

### Window Flags

- `SW_HIDE = 0` - Hide window
- `SW_SHOW = 5` - Show window
- `SW_MINIMIZE = 6` - Minimize
- `SWP_NOMOVE = 0x0002` - Don't move
- `SWP_NOSIZE = 0x0001` - Don't resize

## Building Custom Pranks

### Example 1: Popup Spam

```python
from modules.message_system import SystemMessenger
import time

messenger = SystemMessenger()

for i in range(5):
    messenger.display_popup_thread(
        "Alert",
        f"Alert #{i+1}"
    )
    time.sleep(0.5)
```

### Example 2: Keyboard Block + Message

```python
from modules.keyboard_blocker import KeyboardDisabler
from modules.message_system import SystemMessenger
import time

blocker = KeyboardDisabler()
messenger = SystemMessenger()

blocker.start()
messenger.display_popup("Trapped!", "Your keyboard is blocked!")
time.sleep(3)
blocker.stop()
```

### Example 3: Screenshot Corruption

```python
import pyautogui
from modules.screen_corruptor import ScreenCorruptor

# Take screenshot
screenshot = pyautogui.screenshot()

# Corrupt it
corruptor = ScreenCorruptor()
corrupted = corruptor.corrupt(screenshot, intensity=0.8)

# Save
corrupted.save("corrupted.png")
```

## Performance Optimization

### Image Corruption

**Problem**: Processing large images is slow

**Solution**: Resize first

```python
# Instead of processing 1920x1080
small = image.resize((960, 540))  # 4x faster
corrupted = corruptor.corrupt(small, 0.5)
```

### Threading

**Problem**: Main loop hangs

**Solution**: Use threads for heavy operations

```python
import threading

def heavy_task():
    # Process stuff
    pass

thread = threading.Thread(target=heavy_task, daemon=True)
thread.start()
```

### Event Loops

**Problem**: Pygame freezes while processing

**Solution**: Limit effects per frame

```python
for _ in range(min(10, max_effects)):  # Cap at 10 per frame
    apply_effect()
```

## Troubleshooting

### Pygame Won't Fullscreen

```python
# Try this instead
flags = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
screen = pygame.display.set_mode((width, height), flags)
```

### Keyboard Block Fails Silently

```python
# Debug with:
try:
    blocker.start()
except Exception as e:
    print(f"Error: {e}")
```

### Image Corruption Too Slow

```python
# Reduce iterations
for _ in range(5):  # Was 100
    apply_effect()
```

## Security Considerations

### What This Toolkit Can't Do

❌ Bypass Windows passwords
❌ Access other user accounts
❌ Modify system files
❌ Create persistent backdoors
❌ Survive reboots
❌ Spread to other computers

### What It Can Do

✅ Block user input
✅ Display messages
✅ Corrupt visual display
✅ Hide console window
✅ Create annoying pranks

## Legal Compliance

If you use this:
1. ✅ Own or have permission for the device
2. ✅ Don't use for malicious purposes
3. ✅ Don't violate CFAA or local laws
4. ✅ Document what you're doing
5. ✅ Have a way to stop it

## Advanced Techniques

### Detecting Debuggers

```python
import ctypes

if ctypes.windll.kernel32.IsDebuggerPresent():
    print("Being debugged!")
```

### Process Enumeration

```python
import subprocess

result = subprocess.run(
    ['tasklist'],
    capture_output=True,
    text=True
)
print(result.stdout)
```

### Registry Access

```python
import winreg

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\")
print(winreg.QueryValueEx(key, "Version"))
```

---

For more info, check individual module docstrings! 📚
