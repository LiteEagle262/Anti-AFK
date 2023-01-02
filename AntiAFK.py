import keyboard, os
from colorama import Fore
from time import sleep

enabled = False
last_state = False
count = 0

os.system("title Nest | AntiAFK")
os.system("cls")

print(Fore.YELLOW + """
       d8888          888    d8b            d8888 8888888888 888    d8P  
      d88888          888    Y8P           d88888 888        888   d8P   
     d88P888          888                 d88P888 888        888  d8P    
    d88P 888 88888b.  888888 888         d88P 888 8888888    888d88K     
   d88P  888 888 "88b 888    888        d88P  888 888        8888888b    
  d88P   888 888  888 888    888       d88P   888 888        888  Y88b   
 d8888888888 888  888 Y88b.  888      d8888888888 888        888   Y88b  
d88P     888 888  888  "Y888 888     d88P     888 888        888    Y88b              

                        Made By liteeagle.me                                                                             
""")

toggle_button = input(Fore.GREEN + "Please Type your Toggle Key (EX: F1): ")

os.system("cls")

print(Fore.YELLOW + f"""
       d8888          888    d8b            d8888 8888888888 888    d8P  
      d88888          888    Y8P           d88888 888        888   d8P   
     d88P888          888                 d88P888 888        888  d8P    
    d88P 888 88888b.  888888 888         d88P 888 8888888    888d88K     
   d88P  888 888 "88b 888    888        d88P  888 888        8888888b    
  d88P   888 888  888 888    888       d88P   888 888        888  Y88b   
 d8888888888 888  888 Y88b.  888      d8888888888 888        888   Y88b  
d88P     888 888  888  "Y888 888     d88P     888 888        888    Y88b 
                   Press {toggle_button} to turn on Anti-AFK.
                        Close this to stop it.
                        Made By liteeagle.me                                               
""")

def start():
    while True:
        try:
            keyboard.press_and_release('a')
            sleep(1)
            keyboard.press_and_release('s')
            sleep(1)
            keyboard.press_and_release('space')
            sleep(1)
            keyboard.press_and_release('space')
            sleep(1)
            return start()
        except:
            return start()

while True:
    key_down = keyboard.is_pressed(toggle_button)
    if key_down:
        print(Fore.RED + "Starting Anti-AFK...")
        start()
        break
