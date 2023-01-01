import pyautogui,ctypes
from time import sleep
ctypes.windll.kernel32.SetConsoleTitleW("Nest Anti-AFK")
print("""
       d8888          888    d8b            d8888 8888888888 888    d8P  
      d88888          888    Y8P           d88888 888        888   d8P   
     d88P888          888                 d88P888 888        888  d8P    
    d88P 888 88888b.  888888 888         d88P 888 8888888    888d88K     
   d88P  888 888 "88b 888    888        d88P  888 888        8888888b    
  d88P   888 888  888 888    888       d88P   888 888        888  Y88b   
 d8888888888 888  888 Y88b.  888      d8888888888 888        888   Y88b  
d88P     888 888  888  "Y888 888     d88P     888 888        888    Y88b 
                                                                         
                                                                         
                 Auto Starting In 10 Seconds
                    Close this to stop it!                                                       
""")
def start():
    sleep(10)
    while True:
        sleep(5)
        pyautogui.keyDown(' ')
        pyautogui.keyUp(' ')
        sleep(5)
        pyautogui.keyDown(' ')
        pyautogui.keyUp(' ')
start()
