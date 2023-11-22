# Virtual Screen and Screenshot Guide

These are instructions on how to set up a virtual screen on a Linux system and capture its screenshot using Python and PyAutoGUI.

## Setting Up a Virtual Screen

### Requirements

- Linux system with X11
- VNC Server (e.g., TigerVNC)

### Installation and Configuration

1. **Install a VNC Server:**

   ```
   sudo apt-get update
   sudo apt-get install tigervnc-standalone-server
   ```

2. **Configure and Start the VNC Server:**

   Start the VNC server with a specific resolution:

   ```
   vncserver :1 -geometry 1024x768 -depth 24
   ```

   Replace `1024x768` with the desired screen resolution.

3. **Connecting to the Virtual Screen:**

   - Use `localhost:1` to connect from the same machine.
   - For remote access, use `<IP_ADDRESS>:1`, ensuring proper firewall settings.

## Capturing a Screenshot with PyAutoGUI

### Requirements

- Python
- PyAutoGUI library

### Setup and Usage

1. **Set the DISPLAY Environment Variable (if necessary):**

   ```
   import os
   os.environ['DISPLAY'] = ':1'
   ```

2. **Install PyAutoGUI:**

   ```
   pip install pyautogui
   ```

3. **Capture and Save the Screenshot:**

   ```
   import pyautogui

   screenshot = pyautogui.screenshot()
   screenshot.save('screenshot.png')
   ```

   This script takes a screenshot of the entire screen and saves it as `screenshot.png`.

## Important Notes

- Ensure the Python script has access to the virtual screen's graphical session.
- Adjust firewall and security settings for safe remote access.
- For headless environments, verify that the VNC or virtual screen setup supports graphical operations.
- PyAutoGUI depends on other libraries like `Pillow` for image operations. Ensure all dependencies are installed.