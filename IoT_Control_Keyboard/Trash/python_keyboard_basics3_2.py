from pynput.keyboard import Listener

    

def on_press(key):
    print("Key pressed")

def on_release(key):
    print("Key released")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()