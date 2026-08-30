"""
Keyboard Blocker Module

Blocks keyboard input using pynput.

EXAMPLE:
    from modules.keyboard_blocker import KeyboardDisabler
    
    blocker = KeyboardDisabler()
    blocker.start()  # Block keyboard
    
    # ... do something ...
    
    blocker.stop()   # Unblock keyboard
"""

from pynput import keyboard
import threading
import time


class KeyboardDisabler:
    """
    Disables all keyboard input.
    
    This class uses pynput to intercept and block keyboard events.
    All keys are blocked completely when enabled.
    
    Attributes:
        listener: The keyboard listener thread
        is_running: Whether the blocker is currently active
        keys_pressed: Set of currently pressed keys
    """
    
    def __init__(self):
        """Initialize the keyboard disabler."""
        self.listener = None
        self.is_running = False
        self.keys_pressed = set()
    
    def on_press(self, key):
        """
        Handle key press events.
        
        Args:
            key: The key that was pressed
            
        Returns:
            False to block the key
        """
        try:
            self.keys_pressed.add(key)
            return False  # Block ALL keys
        except:
            return False
    
    def on_release(self, key):
        """
        Handle key release events.
        
        Args:
            key: The key that was released
            
        Returns:
            False to block the key
        """
        try:
            if key in self.keys_pressed:
                self.keys_pressed.discard(key)
        except:
            pass
        return False  # Block on release too
    
    def start(self):
        """
        Start blocking keyboard input.
        
        Starts a background thread that listens for and blocks keyboard events.
        """
        if self.is_running:
            return
        
        self.is_running = True
        
        def run_listener():
            """Run the keyboard listener in a thread."""
            with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release
            ) as self.listener:
                self.listener.join()
        
        thread = threading.Thread(
            target=run_listener,
            daemon=True
        )
        thread.start()
    
    def stop(self):
        """
        Stop blocking keyboard input.
        
        Disables the keyboard listener and allows input again.
        """
        self.is_running = False
        if self.listener:
            self.listener.stop()


# Example usage
if __name__ == "__main__":
    print("Keyboard Blocker Demo")
    print("Blocking keyboard for 3 seconds...")
    
    blocker = KeyboardDisabler()
    blocker.start()
    
    time.sleep(3)
    
    blocker.stop()
    print("Keyboard unblocked!")
