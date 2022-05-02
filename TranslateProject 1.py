from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root=Tk()
root.title("Language project")
root.geometry("700x700")
root.config(bg="blue")
TitleLabel = Label(root,text="LANGUAGE TRANSLATOR", bg="blue", fg="white", font=("Ariel", 15, "bold"))
TitleLabel.place(relx=0.3,rely=0.2,anchor=CENTER)

TextLabel = Label(root,text="Enter text:", bg="blue", fg="white", font=("Times", 10, "bold"))
TextLabel.place(relx=0.25,rely=0.3,anchor=CENTER)

TextInputArea = Text(root, bg="green", fg="white", font=("Times", 9, "bold"), width="50", height="10", wrap=WORD)
TextInputArea.place(relx=0.25,rely=0.45,anchor=CENTER)



languages = LANGUAGES.values()



LanguageDropdown = ttk.Combobox(state="readonly", values=languages, width="30", font=("Times", 9, "bold"))
LanguageDropdown.place(relx=0.35,rely=0.3,anchor=CENTER)
LanguageDropdown.set("English")

OutputLabel = Label(root, text="Output", bg="blue", fg="white", font=("Times", 10, "bold"))
OutputLabel.place(relx=0.75,rely=0.3,anchor=CENTER)

OutputLanguageDropdown = ttk.Combobox(state="readonly", values=languages, width=30, font=("Times", 9, "bold"))
OutputLanguageDropdown.place(relx=0.85,rely=0.3,anchor=CENTER)

OutputBox = Text(root, width="50", height="10", bg="green", fg="white", font=("Times", 9, "bold"))
OutputBox.place(relx=0.75,rely=0.45,anchor=CENTER)

sourceLanguage = LanguageDropdown.get()
destinationLanguage = OutputLanguageDropdown.get()

def Translate():
    Trans = Translator()
    
    try:
        translated = Trans.translate(TextInputArea.get(1.0, END) , src=sourceLanguage, dest=destinationLanguage)
        
        OutputBox.delete(1,END)
        OutputBox.insert(END, translated)
    except:
        print("Try again")
        
TranslateBtn = Button(root,text="Translate", bg="green", fg="white", relief=FLAT, font=("Times", 10, "bold"), command=Translate)
TranslateBtn.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()