#!/usr/bin/env python3
"""
Keyboard Blocker Demo

Demonstrates blocking keyboard input.

Run with: python examples/keyboard_demo.py

WARNING: This will block your keyboard!
Press Ctrl+C multiple times if stuck.
"""

import sys
import os
import time

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.keyboard_blocker import KeyboardDisabler
from modules.message_system import SystemMessenger


def main():
    print("=" * 50)
    print("Python Prank Tools - Keyboard Blocker Demo")
    print("=" * 50)
    print()
    print("⚠️  WARNING: This will block your keyboard!")
    print("If it gets stuck, press Ctrl+C multiple times.")
    print()
    
    messenger = SystemMessenger()
    blocker = KeyboardDisabler()
    
    print("Starting in 3 seconds...")
    time.sleep(3)
    
    print("1. Blocking keyboard...")
    blocker.start()
    
    print("2. Showing popup...")
    messenger.display_popup(
        "Trapped!",
        "Your keyboard is blocked!\n\nTry typing (nothing happens).\n\nIt will unlock in 5 seconds."
    )
    
    print("3. Keyboard blocked for 5 seconds...")
    print("   (Try typing - nothing happens!)")
    time.sleep(5)
    
    print("4. Unblocking keyboard...")
    blocker.stop()
    
    print()
    print("Demo complete! Keyboard is working again.")
    print()
    print("Your keyboard should now work normally.")
    print("Try typing to confirm: ", end="")
    input()
    print("Great! It works!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nForce quit detected.")
        blocker = KeyboardDisabler()
        blocker.stop()
        print("Keyboard unlocked.")
    except Exception as e:
        print(f"Error: {e}")
        blocker = KeyboardDisabler()
        blocker.stop()
