import os, ctypes
import PIL, api, config
from PIL import Image, ImageFilter, ImageDraw, ImageFont

d = os.getcwd() # Get current working dir globally

def set_wallpaper_from_file(filename: str):
    use = os.path.normpath(config.resource_path(filename))
    ctypes.windll.user32.SystemParametersInfoW(20, 0, use, 0)

def generate_wallpaper_and_set():
   image = Image.open(config.resource_path('img/base.png'))
   small = ImageFont.truetype('arial.ttf', 72)
   large = ImageFont.truetype('arial.ttf', 90)
   draw = ImageDraw.Draw(image)
   if config.load_option_from_config('country') != "World":
      draw.text(xy=(815,359), text=str(api.get_country_stats(api.get_country_id(config.load_option_from_config('country')))[0]), fill = (255,255,255), font=large)
      draw.text(xy=(490,680), text=str(api.get_country_stats(api.get_country_id(config.load_option_from_config('country')))[1]), fill = (255,255,255), font=small)
      draw.text(xy=(1265,680), text=str(api.get_country_stats(api.get_country_id(config.load_option_from_config('country')))[2]), fill = (255,255,255), font=small)
   else:
      draw.text(xy=(815,359), text=str(api.get_world_cases()[0]), fill = (255,255,255), font=large)
      draw.text(xy=(490,680), text=str(api.get_world_cases()[1]), fill = (255,255,255), font=small)
      draw.text(xy=(1265,680), text=str(api.get_world_cases()[2]), fill = (255,255,255), font=small)
   image.save(config.resource_path('wallpaper.png'))
   set_wallpaper_from_file('wallpaper.png')
