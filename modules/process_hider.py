"""
Process Hider Module

Hide console windows and disguise process names.

EXAMPLE:
    from modules.process_hider import ProcessHider
    
    hider = ProcessHider()
    hider.hide_console()
    hider.disguise_as("svchost.exe")
"""

import ctypes
import os


class ProcessHider:
    """
    Hide console windows and disguise process names.
    
    This class provides utilities for hiding Python console windows
    and making the process appear as something else.
    
    WARNING: This is for educational purposes. Using this to hide
    malicious processes is illegal.
    """
    
    @staticmethod
    def hide_console():
        """
        Hide the console window.
        
        Hides the Python console window from the taskbar and taskview.
        Works on Windows only.
        
        EXAMPLE:
            ProcessHider.hide_console()
        """
        try:
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            if hwnd != 0:
                # SW_HIDE = 0
                ctypes.windll.user32.ShowWindow(hwnd, 0)
                # Move window off-screen
                ctypes.windll.user32.SetWindowPos(hwnd, 0, -999, -999, 1, 1, 0x0001)
        except Exception as e:
            print(f"Could not hide console: {e}")
    
    @staticmethod
    def disguise_as(process_name):
        """
        Disguise the process as something else.
        
        Changes the console title to appear as a different process.
        This is visual only and doesn't fool proper process inspection.
        
        Args:
            process_name (str): Name to disguise as (e.g., "svchost.exe")
            
        EXAMPLE:
            ProcessHider.disguise_as("explorer.exe")
        """
        try:
            # Change console title
            ctypes.windll.kernel32.SetConsoleTitleW(process_name)
            
            # Try to change window title
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            ctypes.windll.user32.SetWindowTextW(hwnd, process_name)
        except Exception as e:
            print(f"Could not disguise process: {e}")
    
    @staticmethod
    def show_console():
        """
        Show the console window again.
        
        Reverses the hide_console() operation.
        
        EXAMPLE:
            ProcessHider.show_console()
        """
        try:
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            if hwnd != 0:
                # SW_SHOW = 5
                ctypes.windll.user32.ShowWindow(hwnd, 5)
        except Exception as e:
            print(f"Could not show console: {e}")
    
    @staticmethod
    def get_process_id():
        """
        Get the current process ID.
        
        Returns:
            int: The process ID
            
        EXAMPLE:
            pid = ProcessHider.get_process_id()
            print(f"My PID: {pid}")
        """
        return os.getpid()


# Example usage
if __name__ == "__main__":
    print("Process Hider Demo")
    
    pid = ProcessHider.get_process_id()
    print(f"Process ID: {pid}")
    
    print("Hiding console...")
    ProcessHider.hide_console()
    
    print("Disguising as svchost.exe...")
    ProcessHider.disguise_as("svchost.exe")
    
    # Keep running for a bit
    import time
    time.sleep(3)
    
    print("Showing console again...")
    ProcessHider.show_console()
