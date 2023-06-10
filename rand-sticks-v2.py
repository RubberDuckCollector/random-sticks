import random

def rand_controls():

    control_dict = {
        1: "ZR button",
        2: "ZL button",
        3: "R button",
        4: "L button",
        5: "A button",
        6: "B button",
        7: "X button",
        8: "Y button",
        9: "Up D-pad button",
        10: "Down D-pad button",
        11: "Left D-pad button",
        12: "Right D-pad button",
        13: "Plus (+) button",
        14: "Minus (-) button",
        15: "Capture button",
        16: "Right stick press",
        17: "Left stick press"
    }

    sensitivity_dict = {
        1: "-5 sensitivity",
        2: "-4.5 sensitivity",
        3: "-4 sensitivity",
        4: "-3.5 sensitivity",
        5: "-3 sensitivity",
        6: "-2.5 sensitivity",
        7: "-2 sensitivity",
        8: "-1.5 sensitivity",
        9: "-1 sensitivity",
        10: "-0.5 sensitivity",
        11: "0 sensitivity",
        12: "0.5 sensitivity",
        13: "1 sensitivity",
        14: "1.5 sensitivity",
        15: "2 sensitivity",
        16: "2.5 sensitivity",
        17: "3 sensitivity",
        18: "3.5 sensitivity",
        19: "4 sensitivity",
        20: "4.5 sensitivity",
        21: "5 sensitivity"
    }

    msg = ""

    rand_sticks = random.randint(1, 2) # chooses either sticks or motion
    if rand_sticks == 1:
        msg += "Stick controls\n"
        rand_sensitivity = random.sample(list(sensitivity_dict), k=2)
        msg += f"{sensitivity_dict[rand_sensitivity[0]]} vertical\n"
        msg += f"{sensitivity_dict[rand_sensitivity[1]]} horizontal\n"
    else:
        msg += "Motion controls\n"
        rand_sensitivity = random.sample(list(sensitivity_dict), k=1)
        msg += f"{sensitivity_dict[rand_sensitivity[0]]}\n"
    
    controls = random.sample(list(control_dict), k=2)
    msg += f"Swap {control_dict[controls[0]]} with {control_dict[controls[1]]}"

    return msg

print(rand_controls())
