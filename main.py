import api
import wallpaper
import gui
import time


def background():
    wallpaper.generate_wallpaper_and_set()
    gui.w.after(5000, background)


if __name__ == '__main__':
    gui.w.after(5000, background)
    gui.w.mainloop()
