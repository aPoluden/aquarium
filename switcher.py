import argparse

import OPi.GPIO as GPIO

ON, OFF = 1, 0
PIN1, PIN2 = 8, 10

AVAILABLE_ACTIONS = { "on": ON, "off": OFF }
AVAILABLE_DEVICES = {"tank" : PIN1, "tree": PIN2}

GPIO.setwarnings(False)
GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)

def switch(action, device):
    GPIO.setup(AVAILABLE_DEVICES[device], AVAILABLE_ACTIONS[action])
    print("Device - {} is {} now".format(device, action))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simple Switch")
    parser.add_argument("action", choices=["on", "off"])
    parser.add_argument("device", choices=["tank", "tree"])
    args = parser.parse_args()
    switch(args.action, args.device)
