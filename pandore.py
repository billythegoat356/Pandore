# by billythegoat356

# https://github.com/billythegoat356/Pandore


from os import name, chdir
from os.path import isfile
from PIL import Image
from pystyle import Anime, Colorate, Colors, Center, System, Write



if name == 'nt' and __file__:
    path = '/'.join(__file__.split('\\')[:-1])
    chdir(path)



class build:
  def __init__(self, imagepath: str, scale: int) -> None:
    self.path = imagepath
    self.scale = scale

    return self.run()

  def run(self) -> None:
    img = self.mkimage(path=self.path)
    pixels = self.mkpixels(img=img)
    ascii = self.mkascii(pixels=pixels)

    with open(self.npath, mode="w", encoding='utf-8') as f:
      f.write(ascii)
    
    return None

  def mkimage(self, path: str) -> object:
    img = Image.open(path)
    width, height = img.size

    self.nwidth = round(width / self.scale)

    img = img.resize((self.nwidth, round(height / (self.scale * 2))))

    return img.convert('L')

  def mkpixels(self, img: object) -> str:
    pixels = img.getdata()

    pixels = [self.chars[pixel//25] for pixel in pixels]
    return ''.join(pixels).replace('.',' ')

  def mkascii(self, pixels: str) -> str:
    ascii = [pixels[index:index + self.nwidth] for index in range(0, len(pixels), self.nwidth)]
    nascii = []
    for line in ascii:
      if line.strip():
        nascii.append(line)
    return "\n".join(nascii)

  @property
  def npath(self) -> str:
    return ".".join(self.path.split(".")[:-1]) + ".txt"

  @property
  def chars(self) -> str:
    return ["§","/","#","&","@","$","%","*","!",":","."]



ascii = """
.-------.   ____   ,---.   .--.______        ,-----.   .-------.       .-''-. 
 \  _(`)_ \.'  __ `.|    \  |  |    _ `''.  .'  .-,  '. |  _ _   \    .'_ _   \  
 | (_ P._)/   '  \  |  ,  \ |  | _ | ) _  \/ ,-.|O \ _ \| ( ' )  |   / ( ` )   ' 
 |  (_,_) |___|  /  |  |\_ \|  |( ''_'  ) ;  \  '_ /  | |(_ R _) /  . (_ E _)  | 
 |   '-.-'   _.-`   |  _( )_\  | . (D) `. |  _`,/ \ _/  | (_,_).' __|  (_,_)___| 
 |   |    .'   _    | (_ N _)  |(_    ._) : (  '\_/ \   |  |\ \  |  '  \   .---. 
 |   |    |  _( )_  |  (_,_)\  |  (_.\.' / \ `'/. \  ) /|  | \ `'   /\  `-'    / 
 /   )    \ (_ A _) |  |    |  |       .'   '. \_/``'.' |  |  \    /  \       /  
 `---'     '.(_,_).''--'    '--'-----'`       '-----'   ''-'   `'-'    `'-..-' 
"""[1:]


flower = '''
                ..ooo.
             .888888888.
           .888"P""T"T888 8o
         o8o 8.8"8 88o."8o 8o
        88 . o88o8 8 88."8 88P"o
       88 o8 88 oo.8 888 8 888 88
       88 88 88o888" 88"  o888 88
       88."8o."T88P.88". 88888 88
       888."888."88P".o8 8888 888
       "888o"8888oo8888 o888 o8P"
        "8888.""888P"P.888".88P
         "88888ooo  888P".o888
           ""8P"".oooooo8888P
  .oo888ooo.    888PANDORE88
o88888"888"88o.  "8888"".88   .oo888oo..
 8888" "88 88888.       88".o88888888"888.
 "8888o.""o 88"88o.    o8".888"888"88 "88P
  T888C.oo. "8."8"8   o8"o888 o88" ".=888"
   88BILLY8o "8 8 8  .8 .8"88 8"".o888o8P
    "8888C.o8o  8 8  8" 8 o" ...o"""8888
      "88888888 " 8 .8  8   8RASPUTIN8"
        "8888888o  .8o=" o8o..o(8oo88"
            "888" 88"    888888888""
                o8P       "888"""
          ...oo88
 "8oo...oo888""
'''[1:]




System.Size(140, 40)
System.Title("Pandore")
System.Clear()
Anime.Fade(Center.Center(flower), Colors.red_to_green, Colorate.Vertical, interval=0.025, enter=True)



def main():
  System.Clear()
  print("\n"*2)
  print(Colorate.Diagonal(Colors.red_to_green, Center.XCenter(ascii)))
  print("\n"*5)
  
  file = Write.Input("Drag an image -> ", Colors.green_to_yellow, interval=0.005)
  
  if not isfile(file):
      print()
      print(Colorate.Error("Error! This file does not exist!"))
      return

  scale = Write.Input("Enter the scale (recommended: 8) -> ", Colors.green_to_yellow, interval=0.005)
  
  try:
    scale = int(scale)
  except:
    print()
    print(Colorate.Error("Error! The scale has to be an integer"))
    return

  build(imagepath=file, scale=scale)
  
  print()
  Write.Input("Done!", Colors.green_to_yellow, interval=0.005)
  return exit()
        

if __name__ == '__main__':
    while True:
        main()
