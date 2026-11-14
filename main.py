from googletrans import Translator
import tkinter as TK




window = TK.Tk()
window.title("Python-GUI-Calculator")


window.resizable(False, False)

window .title("Tk Example")
window .configure(background="white")
window .geometry("700x800")


def show():
    label.config(text=f"Selected: {listbox.get(ACTIVE)}")

window.mainloop()

# Translator initialisieren
translator = Translator()

text = "Hello, my Name is Tim"

# Übersetzen und ausgeben
translated_text = translator.translate(text=text, src="auto", dest="fr").text
print(translated_text)