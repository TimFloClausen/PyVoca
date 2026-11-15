from deep_translator import MyMemoryTranslator
import tkinter as TK
import asyncio




window = TK.Tk()
window.title("PyVoca")
window.resizable(False, False)
window .configure(background="#17191F")
window .geometry("700x800")



async def Take_input():
    source = language_Selecttions1()
    target = language_Selecttions2()
    INPUT = Text_input.get("1.0", "end-1c")
    print(INPUT)
    if source == "empty" or target == "empty":
        Text_output.delete("1.0", "end")
        Text_output.insert("1.0", "Input Error:")
    else:
        
        translator = MyMemoryTranslator(source, target)
        translated_text = await asyncio.to_thread(translator.translate, INPUT)
        Text_output.delete("1.0", "end")
        Text_output.insert("1.0", translated_text)

def language_Selecttions1():
    source = "empty"
    if clicked1.get() != "Select language":

        if clicked1.get() == "From English":
            source = "english"
            return source
        elif clicked1.get() == "From Spanish":
            source = "spanish"
            return source
        elif clicked1.get() == "From German":
                source = "german"
                return source
        elif clicked1.get() == "From French":
                source = "french"
                return source
    else: 
        source = "empty"
        return source
        

def language_Selecttions2():
    target = "empty"
    if clicked2.get() != "Select language":

        if clicked2.get() == "to English":
            target = "english"
            return target
        elif clicked2.get() == "to Spanish":
            target = "spanish"
            return target
        elif clicked2.get() == "to German":
                target = "german"
                return target
        elif clicked2.get() == "to French":
                target = "french"
                return target
    else:
        target = "empty"
        return target



    
language_options_1 = [
    "Select language",
    "From English",
    "From Spanish",
    "From German",
    "From French"
    ]
clicked1 = TK.StringVar()
clicked1.set("Select language")


language_options_2 = [

    
    
    "Select language",
    "to English",
    "to Spanish",
    "to German",
    "to French"
    ]

clicked2 = TK.StringVar()
clicked2.set("Select language")

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
