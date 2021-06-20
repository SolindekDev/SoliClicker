# Clicker by SolindekDev on github
# https://github.com/SolindekDev/
# License MIT!
# I started with Python

# Import modules
import keyboard
import time
import mouse

# Welcom message
print("To make activate macro, click the R button")

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
                print('Macro on')
                macroCheck = False
                time.sleep(0.2)
            elif macroCheck == False:
                print('Macro off')
                macroCheck = True
                time.sleep(0.2)
    except:
        
