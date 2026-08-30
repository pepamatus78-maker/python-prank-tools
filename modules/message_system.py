"""
Message System Module

Create Windows system message popups.

EXAMPLE:
    from modules.message_system import SystemMessenger
    
    messenger = SystemMessenger()
    messenger.display_popup("Title", "This is a message")
"""

import ctypes
import threading


class SystemMessenger:
    """
    Create system message popups.
    
    Uses Windows API to create native message boxes that look like
    system messages.
    
    Attributes:
        messages: List of random messages to use
    """
    
    def __init__(self):
        """Initialize the messenger with default messages."""
        self.messages = [
            "⚠️  SYSTEM: Access Denied",
            "🔒 SECURITY: Unauthorized access attempt",
            "💀 FATAL ERROR: Process failed",
            "🚨 ALERT: System integrity compromised",
            "⛔ SYSTEM LOCKED: Admin required",
            "🔴 CRITICAL: Operation blocked",
            "📍 TRACKER: System monitoring active",
            "💻 SYSTEM: Action required",
            "⚠️  WARNING: Access denied",
            "🔐 LOCKED: Cannot close window",
        ]
    
    def add_message(self, message):
        """
        Add a custom message to the pool.
        
        Args:
            message (str): The message to add
        """
        self.messages.append(message)
    
    def get_random_message(self):
        """
        Get a random message from the pool.
        
        Returns:
            str: A random message
        """
        import random
        return random.choice(self.messages)
    
    def display_popup(self, title, message):
        """
        Display a system message popup.
        
        Args:
            title (str): The popup title
            message (str): The popup message
            
        EXAMPLE:
            messenger = SystemMessenger()
            messenger.display_popup("Error", "Something went wrong!")
        """
        try:
            ctypes.windll.user32.MessageBoxW(
                0,
                message,
                title,
                0x00000000  # OK button only
            )
        except:
            print(f"[{title}] {message}")
    
    def display_popup_thread(self, title, message):
        """
        Display a popup in a separate thread (non-blocking).
        
        Args:
            title (str): The popup title
            message (str): The popup message
        """
        thread = threading.Thread(
            target=self.display_popup,
            args=(title, message),
            daemon=True
        )
        thread.start()
    
    def display_uac_popup(self):
        """
        Display a fake UAC (User Account Control) popup.
        
        Returns:
            int: User response (usually 6 for Yes, 7 for No)
        """
        try:
            message = (
                "Windows Security\n\n"
                "User Account Control\n\n"
                "Do you want to allow this app to make changes?\n\n"
                "Verified publisher: Microsoft Corporation\n"
                "This program requires administrator privileges."
            )
            
            result = ctypes.windll.user32.MessageBoxW(
                0,
                message,
                "User Account Control",
                0x00000030  # Warning icon with Yes/No
            )
            
            return result
        except:
            return None


# Example usage
if __name__ == "__main__":
    print("Message System Demo")
    
    messenger = SystemMessenger()
    
    # Simple popup
    messenger.display_popup("Demo", "Hello from Python!")
    
    # Random message
    msg = messenger.get_random_message()
    messenger.display_popup("Random", msg)
    
    # Fake UAC
    print("Showing UAC popup...")
    result = messenger.display_uac_popup()
    print(f"Result: {result}")
