import keyboard, os, ctypes
from colorama import Fore
from time import sleep

ctypes.windll.kernel32.SetConsoleTitleW("Nest | AntiAFK")

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
                   Press {toggle_button} to toggle the Anti-AFK.
                        Made By liteeagle.me                                               
""")

running = False

def start_stop():
    global running
    if running:
        running = False
        print(Fore.RED + "Stopping Anti-AFK...")
    else:
        running = True
        print(Fore.BLUE + "Starting Anti-AFK...")

keyboard.add_hotkey(toggle_button, start_stop)

while True:
    if running:
        try:
            sleep(1)
            keyboard.press_and_release('space')
            sleep(1)
            keyboard.press_and_release('space')
            sleep(1)
            pass
        except:
            pass
