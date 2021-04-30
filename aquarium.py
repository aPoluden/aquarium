import argparse

import OPi.GPIO as GPIO

ON, OFF = 0, 1
COMPRESSOR, PUMP = 8, 10
devices = [COMPRESSOR, PUMP]

GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)

# @check_is_safe 
def _turn_on():
    for device in devices:
        GPIO.setup(device, ON)
    print("turned on")

# @check_is_safe
def _turn_off():
    for device in devices:
        GPIO.setup(device, OFF)
    print("turn off")

actions = {"on": _turn_on, "off": _turn_off}

def app(action):
    actions[action]()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='On/Off Aquarium')
    parser.add_argument("action", choices=["on", "off"])
    args = parser.parse_args()
    app(args.action)
