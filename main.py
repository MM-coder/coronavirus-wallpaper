import api, wallpaper, gui, time


def background():
    while 1: 
        wallpaper.generate_wallpaper_and_set()
        time.sleep(5)


if __name__ == '__main__':
    gui.w.mainloop()
    background()