from googletrans import Translator
import tkinter as TK




window = TK.Tk()
window.title("PyVoca")
window.resizable(False, False)
window .configure(background="#363636")
window .geometry("700x800")

    
language_options_1 = [
    "Select source language",
    "Englisch",
    "Spain",
    "German",
    "France"
    ]
clicked1 = TK.StringVar()
clicked1.set("Select source language")


language_options_2 = [

    
    
    "Select target language",
    "Englisch",
    "Spain",
    "German",
    "France"
    ]

clicked2 = TK.StringVar()
clicked2.set("Select ctarget language")

Text_input = TK.Text(window, bg = "#878787", fg = "black", height = 10, width = 10, font = "Ariel")

window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)


drop1 = TK.OptionMenu(window, clicked1, *language_options_1)
drop1.grid(row = 0, column = 0)

drop2 = TK.OptionMenu(window, clicked2, *language_options_2)

drop2.grid(row = 0, column = 2)

Text_input.grid(row = 2, column = 0)




window.mainloop()

# Translator initialisieren
translator = Translator()

text = "Hello, my Name is Tim"

# Übersetzen und ausgeben
translated_text = translator.translate(text=text, src="auto", dest="fr").text
print(translated_text)