#!/usr/bin/env python3
"""
Simple Popup Demo

Demonstrates the message system module.

Run with: python examples/popup_demo.py
"""

import sys
import os
import time

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.message_system import SystemMessenger


def main():
    print("=" * 50)
    print("Python Prank Tools - Popup Demo")
    print("=" * 50)
    print()
    
    messenger = SystemMessenger()
    
    print("1. Showing simple popup...")
    messenger.display_popup(
        "Hello!",
        "Welcome to Python Prank Tools!\n\nThis is a simple popup."
    )
    
    print("2. Showing warning popup...")
    time.sleep(1)
    messenger.display_popup(
        "⚠️  Warning",
        "This is a warning popup.\n\nNothing bad is happening!"
    )
    
    print("3. Showing error popup...")
    time.sleep(1)
    messenger.display_popup(
        "❌ Error",
        "This is an error popup.\n\nStill harmless!"
    )
    
    print("4. Showing custom message...")
    time.sleep(1)
    msg = messenger.get_random_message()
    messenger.display_popup("Random Message", msg)
    
    print("\nDemo complete!")
    print("\nTip: You can customize messages by:")
    print("  messenger.add_message('Your custom message')")
    print()


if __name__ == "__main__":
    main()
