from deep_translator import MyMemoryTranslator
import tkinter as TK
import asyncio




window = TK.Tk()
window.title("PyVoca")
window.resizable(False, False)
window .configure(background="#17191F")
window .geometry("1200x800")



async def Take_input():
    source = language_Selecttions1()
    target = language_Selecttions2()
    INPUT = Text_input.get("1.0", "end-1c")
    if source == "empty" or target == "empty":
        Text_output.delete("1.0", "end")
        Text_output.insert("1.0", "Input Error:")
    else:
        
        translator = MyMemoryTranslator(source, target)
        translated_text = await asyncio.to_thread(translator.translate, INPUT)
        Text_output.delete("1.0", "end")
        Text_output.insert("1.0", translated_text)

def clear_text():
    Text_input.delete("1.0", "end")
    Text_output.delete("1.0", "end")

def get_txt():

    original_text = Text_input.get("1.0", "end-1c").splitlines()
    translated_text = Text_output.get("1.0", "end-1c").splitlines()

    with open("Output.txt", "w", encoding="utf-8") as text_file:
        for i in range(len(original_text)):
            text_file.write(f"{original_text[i]}\t{translated_text[i]}\n")

def get_tutorial():
    
    tutorial_text = ("""
    How to use PyVoca

    Using PyVoca is really easy!
    
    1. Choose your source and target languages.
    
    2. Write the words you want to learn in your source language.
    
    3. Translate them using the Translate button.
    
    4. Edit the translations if necessary.
    
    5. Click on Cards to export your vocabulary into a .txt file.
    
    6. C/P the text from the .txt file into Quizlet's import section.
    
    7. Start learning with your flashcards!
    
    Note: The text in the source language should look like this:

    Vocabulary 1
    Vocabulary 2
    Vocabulary 3
    Vocabulary 4
    Vocabulary 5
                    """)
    Text_input.delete("1.0", "end")
    Text_input.insert("1.0",tutorial_text)
    

     




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
        elif clicked1.get() == "From Italian":
                source = "italian"
                return source
        elif clicked1.get() == "From Japanese":
                source = "japanese"
                return source
        elif clicked1.get() == "From Latin":
                source = "latin"
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
        elif clicked2.get() == "to Italian":
            target = "italian"
            return target
        elif clicked2.get() == "to Japanese":
            target = "japanese"
            return target
        elif clicked2.get() == "to Latin":
            target = "latin"
            return target
    else:
        target = "empty"
        return target



    
language_options_1 = [
    "Select language",
    "From English",
    "From Spanish",
    "From German",
    "From French",
    "From Italian",
    "From Japanese",
    "From Latin"
    ]
clicked1 = TK.StringVar()
clicked1.set("Select language")


language_options_2 = [
    "Select language",
    "to English",
    "to Spanish",
    "to German",
    "to French",
    "to Italian",
    "to Japanese",
    "to Latin"
]

clicked2 = TK.StringVar()
clicked2.set("Select language")

frame = TK.Frame(window, bg= "#17191F", width=200, height=500, bd=3,)
frame.grid(row = 1, column = 1)

button_translate = TK.Button(frame, bg = "#6385F5", height = 3, width = 7,
                            text="Translate", font = "Segoe",
                            command = lambda: asyncio.run(Take_input()))

button_clear = TK.Button(frame, bg = "#6385F5", height = 3, width = 7,
                        text="Clear", font = "Segoe",
                        command = lambda: clear_text())


button_file = TK.Button(frame, bg = "#6385F5", height = 3, width = 7,
                        text="Cards", font = "Segoe",
                        command = lambda: get_txt())

button_tutorial = TK.Button(frame, bg = "#6385F5", height = 3, width = 7,
                        text="Tutorial", font = "Segoe",
                        command = lambda: get_tutorial())



Text_input = TK.Text(window, bg = "#222630", fg = "#F1F3F9",
                     height = 40, width = 50, font = "Segoe",)
Text_output = TK.Text(window, bg = "#222630", fg = "#F1F3F9",
                      height = 40, width = 50, font = "Segoe",)

window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)


window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)
window.rowconfigure(3, weight = 1)


drop1 = TK.OptionMenu(window, clicked1, *language_options_1)
drop1.grid(row = 0, column = 0, pady= 5)

drop2 = TK.OptionMenu(window, clicked2, *language_options_2)

drop2.grid(row = 0, column = 2, pady= 5)

Text_input.grid(row = 1, column = 0)
Text_output.grid(row = 1, column = 2)


button_tutorial.grid(row=0, column=0, pady=25)
button_translate.grid(row=1, column=0, pady=25)
button_clear.grid(row=2, column=0, pady=25)
button_file.grid(row=3, column=0, pady=25)








window.mainloop()
