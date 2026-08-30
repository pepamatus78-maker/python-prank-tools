#!/usr/bin/env python3
"""
Process Hider Demo

Demonstrates hiding the console window.

Run with: python examples/process_hider_demo.py
"""

import sys
import os
import time

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.process_hider import ProcessHider


def main():
    print("=" * 50)
    print("Python Prank Tools - Process Hider Demo")
    print("=" * 50)
    print()
    
    # Get process info
    pid = ProcessHider.get_process_id()
    print(f"Current Process ID: {pid}")
    print()
    
    print("1. Disguising as 'svchost.exe'...")
    ProcessHider.disguise_as("svchost.exe")
    print("   Check the window title - it changed!")
    print()
    
    time.sleep(2)
    
    print("2. Hiding console window in 3 seconds...")
    print("   (The console will disappear but the program still runs)")
    print()
    
    for i in range(3):
        print(f"   {3-i}...")
        time.sleep(1)
    
    # Hide the console
    ProcessHider.hide_console()
    
    # Keep running for 5 seconds
    print("   [Hidden console - running for 5 more seconds]")
    time.sleep(5)
    
    # Show it again
    print("3. Showing console again...")
    ProcessHider.show_console()
    
    print()
    print("Demo complete!")
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        ProcessHider.show_console()  # Make sure console is visible
