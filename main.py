from googletrans import Translator
import tkinter as TK




window = TK.Tk()
window.title("PyVoca")
window.resizable(False, False)
window .configure(background="white")
window .geometry("700x800")

language_options = [
    "Select source language",
    "Englisch",
    "Spain",
    "German",
    "France"
    ]

clicked = TK.StringVar()
clicked.set("Select source language")

drop1 = TK.OptionMenu(window, clicked, *language_options)
drop1.pack()





window.mainloop()

# Translator initialisieren
translator = Translator()

text = "Hello, my Name is Tim"

# Übersetzen und ausgeben
translated_text = translator.translate(text=text, src="auto", dest="fr").text
print(translated_text)