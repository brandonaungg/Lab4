from time import sleep
import time
from hal import hal_led as led
from hal import hal_input_switch as sw


def main():
    sw.init()
    led.init()

    while True:
        i = 0
        if(sw.read_slide_switch()==1):
            led.set_output(0,1)
            sleep(0.2)

            led.set_output(0, 0)
            sleep(0.2)

        elif(sw.read_slide_switch()==0):
            start=time.time()
            seconds=5
            while True:
                current=time.time()
                elapsed=current-start
                led.set_output(0, 1)
                sleep(0.1)
                led.set_output(0, 0)
                sleep(0.1)
                if elapsed>seconds:
                    led.set_output(0, 0)

main()