import RPi.GPIO as g
import time

g.setmode(g.BOARD)
g.setup(15,g.OUT)
g.output(15, True)

time.sleep(10)
g.cleanup()
