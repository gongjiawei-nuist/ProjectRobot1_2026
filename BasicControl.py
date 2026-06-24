from microbit import *
import tinybit

BASE_SPEED = 160

def execute_step(direction, speed, duration):
  
    print("Action: {}, Speed: {}, Time: {}ms".format(direction, speed, duration))
    
    if direction == "forward":
        tinybit.car_run(speed)
        display.show(Image.ARROW_N)
    elif direction == "backward":
        tinybit.car_back(speed)
        display.show(Image.ARROW_S)
    elif direction == "left":
        tinybit.car_left(speed)
        display.show(Image.ARROW_W)
    elif direction == "right":
        tinybit.car_right(speed)
        display.show(Image.ARROW_E)
    elif direction == "stop":
        tinybit.car_stop()
        display.clear()
        return True

    check_interval = 50
    elapsed_time = 0
    
    while elapsed_time < duration:
        if button_b.is_pressed():
            print("Emergency Stop Triggered during movement!")
            tinybit.car_stop()
            display.clear()
            return False 
            
        sleep(check_interval)
        elapsed_time += check_interval
        
    return True  

def run_custom_path():
    """
    Run the predefined sequence of movements.
    """
    user_defined_path = [
        ("forward", BASE_SPEED, 3000),
        ("right", BASE_SPEED, 1000),
        ("forward", BASE_SPEED, 2000),
        ("left", BASE_SPEED, 1000),
        ("backward", BASE_SPEED, 2000)
    ]
    
    for step in user_defined_path:
        success = execute_step(step[0], step[1], step[2])
        if not success:
            print("Path sequence aborted.")
            return  
            
    execute_step("stop", 0, 0)
    print("Path sequence completed.")


if name=="main":
    display.show(Image.HAPPY)
    print("System Ready. Press Button A to start.")
    
    while True:
        if button_a.is_pressed():
            print("Starting path execution...")
            run_custom_path()
            
        if button_b.is_pressed():
            tinybit.car_stop()
            display.clear()
            
        sleep(100)
