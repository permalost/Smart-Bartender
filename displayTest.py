import time
import display

screen = display.Display()

screen.clear()

for p in range(0, 101, 2):
    time.sleep(.1)
    print(p)
    screen.displayOnUpperMid(str(p))
    screen.displayOnLowerMid(str(p))
    screen.displayOnBottom(str(p))
    screen.progressbar(p)
