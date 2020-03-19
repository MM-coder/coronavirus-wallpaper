import tkinter, api, config, wallpaper
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image


w = tkinter.Tk()

menubar = Menu(w)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=w.quit)
menubar.add_cascade(label="File", menu=filemenu)

def about():
    top = Toplevel(bg = '#081421')
    img = ImageTk.PhotoImage(Image.open("img/mark.png"))
    img_panel = Label(top, image = img, bg = '#081421')
    img_panel.pack(pady=10)
    description = Label(top, text="Made to have an easy way to track\n coronavirus cases in your area", fg="white", bg="#081421")
    description.pack(expand="no")
    size = 15, 15
    # Website Social
    adress = Label(top, text="You can find me at https://maurom.dev/", fg="white", bg="#081421" )
    adress.pack()
    # Github Social
    github = ImageTk.PhotoImage(Image.open("img/github.png").resize(size))
    g_icon = Label(top, image=github, bg="#081421")
    at = Label(top, text="@MM-coder", fg="white", bg="#081421" )
    g_icon.pack(side=LEFT, padx=10)
    at.pack(side=LEFT)
    top.title("About")
    top.geometry("320x200")
    top.mainloop()


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)



current_var = StringVar(w)
current_var.set(f"Your current country is {config.load_option_from_config('country')}")

current = ttk.Label(w, textvariable=current_var)
current.pack()

country = StringVar(w)
country.set("World") # initial value
country_list = api.get_country_list()
option = ttk.Combobox(w, values=country_list)
option.current(country_list.index(config.load_option_from_config('country')))
option.pack(padx=10, pady=10)

def confirm():
    config.write_option_to_config('country', option.get())
    current_var.set(f"Your current country is {config.load_option_from_config('country')}")


confirm = ttk.Button(w, text="Change Country", command=confirm)
confirm.pack(padx=20)

def force_update():
    wallpaper.generate_wallpaper_and_set()
    showinfo("Action Complete", "Wallpaper has been set!")

confirm = ttk.Button(w, text="Set Wallpaper", command=force_update)
confirm.pack(padx=20)

w.title("Coronavirus Wallpaper")
w.iconbitmap(default='img/virus.ico')
w.config(menu=menubar)
w.geometry("320x200")