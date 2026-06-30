import keyboard
import time


def press_space():
    keyboard.press("space")
    time.sleep(0.05)
    keyboard.release("space")


def trigger():
    press_space()

    time.sleep(0.35)

    press_space()

    time.sleep(0.2)

    press_space()


print("Bereit. ENTER drücken für 3 Space-Klicks.")

keyboard.on_press_key("enter", lambda e: trigger())

keyboard.wait()