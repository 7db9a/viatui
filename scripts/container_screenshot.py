import pyautogui
import time
from modules.screenshot_grid import create_screenshot_with_grid

# Set the DISPLAY environment variable if necessary
# os.environ['DISPLAY'] = ':1'

if __name__ == '__main__':
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chrome-screenshot1.png')
  #pyautogui.moveTo(700, 450)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chrome-screenshot2.png')
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chrome-screenshot3.png')

  ## Click on settings menu (triple dots in a row)
  #pyautogui.moveTo(975, 65)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chrome-screenshot4.png')

  ## Click on `Extensions`
  #pyautogui.moveTo(700, 283)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chrome-screenshot5.png')

  ## Click on `Manage Extensions`
  #pyautogui.moveTo(550, 283)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chrome-screenshot6.png')

  ## Switch 'Developer Mode' on
  #pyautogui.moveTo(985, 112)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chrome-screenshot7.png')

  ## Click 'Load unpacked'
  #pyautogui.moveTo(100 , 175)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chrome-screenshot8.png')

  ## Click 'app' directory
  #pyautogui.moveTo(50, 150)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chrome-screenshot9.png')

  ## Click 'dist-chrome-extension
  #pyautogui.moveTo(200, 125)
  #pyautogui.doubleClick()
  #time.sleep(2)
  #pyautogui.moveTo(350, 50)
  #pyautogui.click()
  #pyautogui.press('enter')
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chrome-screenshot10.png')

  ## Click extension button


  pyautogui.moveTo(890, 60)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chrome-screenshot11.png')

  
