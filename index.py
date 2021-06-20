# Clicker by SolindekDev on github
# https://github.com/SolindekDev/
# License MIT!
# I started with Python

# Import modules
import keyboard
import time
import mouse

# Welcom message
print("Aby uruchomić macro kliknij przycisk R")

# Important variable!
macroCheck = False

# While to see if R is pressed
while True:
    if macroCheck == True:
        mouse.click('left') 
        time.sleep(0.09)
    try:
        # If pressed
        if keyboard.is_pressed('r'):
            # Action on pressed
            if macroCheck == True: 
                print('Wyłączono macro')
                macroCheck = False
                time.sleep(0.2)
            elif macroCheck == False:
                print('Włączono macro')
                macroCheck = True
                time.sleep(0.2)
    except:
        print('kliknięto inny klawisz')
