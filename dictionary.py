import json
from tkinter import *
from difflib import get_close_matches

window = Tk()
window.title("English Dictionary")
window.geometry("800x400")
window.iconbitmap("icon.ico")
window.configure(bg="#e8daef")
frame1 = Frame(window, bg="#e8daef")
frame2 = Frame(window, bg="#e8daef")


data = json.load(open("data.json"))

    
def w():
    
    global data
    b_y.pack_forget()
    b_n.pack_forget()
    
    word = search.get().lower()
    
    
    
    if word in data:
        meaning = data[word]
        definition.config(text=list(word) + meaning)
        search.delete(0,"end")
    elif word not in data:
        try:
            
            m = get_close_matches(word,data.keys())[0]
            t = ("Did you mean - ")
            w = t + m + "?"
            definition.config(text=w)
            b_y.pack()
            b_n.pack()
        except IndexError as error:
            definition.config(text="Such word does not exist")
    else:
        pass
    
      
def y():
    global data, search
    word = search.get().lower()
    m = get_close_matches(word,data.keys())[0]
    
    if m in data:
        meaning = data[m]
        definition.config(text=list(m) + meaning)
    else:
        definition.config(text="Sorry, try another word.")
    b_y.pack_forget()
    b_n.pack_forget()
    search.delete(0,"end")


def n():
    definition.config(text="Sorry, I don't know this word\nPlease try another!")
    b_y.pack_forget()
    b_n.pack_forget()
    

label = Label(frame1, text="Write your word here:", font=("Times", 20), bg="#e8daef")
search = Entry(frame1, borderwidth=4, font=("Times", 14))
button = Button(frame1, borderwidth=4, font=("Times", 14), text="Search", command=w)

definition = Label(frame2, wraplength = 700, justify = "left", bg="#e8daef", font=("Times", 14))

b_y = Button(frame2, text="Yes", command=y)
b_n = Button(frame2, text="No", command=n)

label.pack(side="top")
search.pack(side="top")
button.pack(side="top")
definition.pack(side="top")

search.bind('<Return>',(lambda event: w()))
frame1.pack(side="top")
frame2.pack(side="top")
window.mainloop()
