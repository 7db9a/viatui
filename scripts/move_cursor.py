import pyautogui
import time

# Calculate the coordinates
grid_size = 100  # Grid size in pixels
column_index = 3  # Column of the vertex
row_index = 4    # Row of the vertex

x_coordinate = column_index * grid_size
y_coordinate = row_index * grid_size

# Move the cursor to the specified vertex
pyautogui.moveTo(x_coordinate, y_coordinate)

# Optional: a short pause to see the cursor move before the click
#time.sleep(1)
#
## Click at the current position
#pyautogui.click()
