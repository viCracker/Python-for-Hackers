import random
import time

drill = ["MOVE HEAD LEFT", "MOVE HEAD RIGHT", "RIGHT JAB", "LEFT JAB", "LEFT HOOK", "RIGHT HOOK", "ANY UPPER-CUT", "LEFT UPPER-CUT", "RIGHT UPPER-CUT"]
timer = float(input("How long you wanna train(sec): "))

while timer > 0:
    print(random.choice(drill))
    time.sleep(2)
    timer -= 2
