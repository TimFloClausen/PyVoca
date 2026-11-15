from googletrans import Translator
import tkinter as TK
import asyncio




window = TK.Tk()
window.title("PyVoca")
window.resizable(False, False)
window .configure(background="#17191F")
window .geometry("700x800")


async def Take_input():
    INPUT = Text_input.get("1.0", "end-1c")
    print(INPUT)
    translator = Translator()
    translated = await translator.translate("hello world", src="en", dest="fr")
    print(translated.__dict__)



    
language_options_1 = [
    "Select language",
    "to English",
    "to Spainish",
    "to German",
    "to France"
    ]
clicked1 = TK.StringVar()
clicked1.set("Select language")


language_options_2 = [

    
    
    "Select language",
    "to English",
    "to Spainish",
    "to German",
    "to France"
    ]

clicked2 = TK.StringVar()
clicked2.set("Select languagee")

button_translate = TK.Button(window, bg = "#6385F5", height = 3, width = 10,
                            text="Translate", font = "Segoe",
                            command = lambda: asyncio.run(Take_input()))


button_file = TK.Button(window, bg = "#6385F5", height = 3, width = 10,
                        text="Cards", font = "Segoe")

Text_input = TK.Text(window, bg = "#222630", fg = "#F1F3F9",
                     height = 35, width = 25, font = "Segoe",)
Text_output = TK.Text(window, bg = "#222630", fg = "#F1F3F9",
                      height = 35, width = 25, font = "Segoe",)

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

Text_input.grid(row = 1, column = 0)

Text_output.grid(row = 1, column = 2)

button_translate.grid(row = 0, column = 1)
button_file.grid(row = 1, column = 1)







window.mainloop()
