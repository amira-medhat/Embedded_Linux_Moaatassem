import pyautogui
import time
import os

def open_vscode():
    """Open Visual Studio Code."""
    # Replace with the command/path to open VSCode on your system
    os.system("code")  # This assumes 'code' command is available in PATH
    time.sleep(1)

def install_extension(extension_name):
    """Install the specified extension in VSCode."""
    # Open the extensions panel
    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)
    
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(2)

    # Search for the extension
    pyautogui.write(extension_name)
    time.sleep(2)
    
    # Press Enter to search
    pyautogui.press('enter')
    time.sleep(2)
    
    # Move to the Install button (this might need adjustments based on your screen resolution)
    pyautogui.moveTo(730, 295)
    pyautogui.click()
    time.sleep(5)  # Wait for the installation to complete


def main():
    # Open VSCode
    open_vscode()
    
    # Wait for VSCode to open
    time.sleep(10)
    
    # List of extensions to install
    extensions = [
        "clangd",
        "c++ testmate",
        "c++ helper",
        "cmake",
        "cmake tools"
    ]
    
    for ext in extensions:
        install_extension(ext)
    
    print("All extensions installed successfully.")

if __name__ == "__main__":
    main()

