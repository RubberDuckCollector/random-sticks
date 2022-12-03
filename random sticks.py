from random import randint

def rand_sticks():
    randSticksSense = randint(1, 21)
    randHorizontalStickInverted = randint(0, 1)
    randVerticalStickInverted = randint(0, 1)
    
    if randSticksSense == 1:
      print("sticks sensitivity -5")
    elif randSticksSense == 2:
      print("sticks sensitivity -4.5")
    elif randSticksSense == 3:
      print("sticks sensitivity -4")
    elif randSticksSense == 4:
      print("sticks sensitivity -3.5")
    elif randSticksSense == 5:
      print("sticks sensitivity -3")
    elif randSticksSense == 6:
      print("sticks sensitivity -2.5")
    elif randSticksSense == 7:
      print("sticks sensitivity -2")
    elif randSticksSense == 8:
      print("sticks sensitivity -1.5")
    elif randSticksSense == 9:
      print("sticks sensitivity -1")
    elif randSticksSense == 10:
      print("sticks sensitivity -0.5")
    elif randSticksSense == 11:
      print("sticks sensitivity 0")
    elif randSticksSense == 12:
      print("sticks sensitivity 0.5")
    elif randSticksSense == 13:
      print("sticks sensitivity 1")
    elif randSticksSense == 14:
      print("sticks sensitivity 1.5")
    elif randSticksSense == 15:
      print("sticks sensitivity 2")
    elif randSticksSense == 16:
      print("sticks sensitivity 2.5")
    elif randSticksSense == 17:
      print("sticks sensitivity 3")
    elif randSticksSense == 18:
      print("sticks sensitivity 3.5")
    elif randSticksSense == 19:
      print("sticks sensitivity 4")
    elif randSticksSense == 20:
      print("sticks sensitivity 4.5")
    elif randSticksSense == 21:
      print("sticks sensitivity 5")
      
    if randHorizontalStickInverted == 1:
      print("inverted horizontal stick")
    
    if randVerticalStickInverted == 1:
      print("inverted vertical stick")
    
    randButton1 = randint(1, 17)
    if randButton1 == 1:
      randButton1 = "ZR button"
    elif randButton1 == 2:
      randButton1 = "L button"
    elif randButton1 == 3:
      randButton1 = "minus (-) button"
    elif randButton1 == 4:
      randButton1 = "capture button"
    elif randButton1 == 5:
      randButton1 = "left stick press"
    elif randButton1 == 6:
      randButton1 = "up d-pad button"
    elif randButton1 == 7:
      randButton1 = "left d-pad button"
    elif randButton1 == 8:
      randButton1 = "down d-pad button"
    elif randButton1 == 9:
      randButton1 = "right d-pad button"
    elif randButton1 == 10:
      randButton1 = "ZR button"
    elif randButton1 == 11:
      randButton1 = "R button"
    elif randButton1 == 12:
      randButton1 = "plus (+) button"
    elif randButton1 == 13:
      randButton1 = "X button"
    elif randButton1 == 14:
      randButton1 = "A button"
    elif randButton1 == 15:
      randButton1 = "B button"
    elif randButton1 == 16:
      randButton1 = "Y button"
    elif randButton1 == 17:
      randButton1 = "right stick press"
    
    randButton2 = randint(1, 17)
    if randButton2 == 1:
      randButton2 = "ZL button"
    elif randButton2 == 2:
      randButton2 = "L button"
    elif randButton2 == 3:
      randButton2 = "minus (-) button"
    elif randButton2 == 4:
      randButton2 = "capture button"
    elif randButton2 == 5:
      randButton2 = "left stick press"
    elif randButton2 == 6:
      randButton2 = "up d-pad button"
    elif randButton2 == 7:
      randButton2 = "left d-pad button"
    elif randButton2 == 8:
      randButton2 = "down d-pad button"
    elif randButton2 == 9:
      randButton2 = "right d-pad button"
    elif randButton2 == 10:
      randButton2 = "ZR button"
    elif randButton2 == 11:
      randButton2 = "R button"
    elif randButton2 == 12:
      randButton2 = "plus (+) button"
    elif randButton2 == 13:
      randButton2 = "X button"
    elif randButton2 == 14:
      randButton2 = "A button"
    elif randButton2 == 15:
      randButton2 = "B button"
    elif randButton2 == 16:
      randButton2 = "Y button"
    elif randButton2 == 17:
      randButton2 = "right stick press"
    
    print(f"\nswap {randButton1} with {randButton2}")

rand_sticks()