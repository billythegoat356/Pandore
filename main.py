from requests import post, delete
from terminaltables import DoubleTable
from pystyle import *


def maketable(dictionnary: dict, title: str, space: str = " "):
    table = [(space + str(key) if len(str(key)) == 1 else str(key), value)
             for key, value in dictionnary.items()]
    return DoubleTable(table_data=table, title=title)

table = {
    "...": "Choose a mode",
    "1": "Upload a new Bot",
    "2": "Delete your Bot",
    "3": "Choose an other code"
}
modes = maketable(table, "Modes").table


ascii = """
.-------.   ____   ,---.   .--.______        ,-----.   .-------.       .-''-. 
 \  _(`)_ \.'  __ `.|    \  |  |    _ `''.  .'  .-,  '. |  _ _   \    .'_ _   \  
 | (_ o._)/   '  \  |  ,  \ |  | _ | ) _  \/ ,-.|  \ _ \| ( ' )  |   / ( ` )   ' 
 |  (_,_) |___|  /  |  |\_ \|  |( ''_'  ) ;  \  '_ /  | |(_ o _) /  . (_ o _)  | 
 |   '-.-'   _.-`   |  _( )_\  | . (_) `. |  _`,/ \ _/  | (_,_).' __|  (_,_)___| 
 |   |    .'   _    | (_ o _)  |(_    ._) : (  '\_/ \   |  |\ \  |  '  \   .---. 
 |   |    |  _( )_  |  (_,_)\  |  (_.\.' / \ `'/. \  ) /|  | \ `'   /\  `-'    / 
 /   )    \ (_ o _) |  |    |  |       .'   '. \_/``'.' |  |  \    /  \       /  
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
   88888888o "8 8 8  .8 .8"88 8"".o888o8P
    "8888C.o8o  8 8  8" 8 o" ...o"""8888
      "88BILLY8 " 8 .8  8   888LOTUS888"
        "8888888o  .8o=" o8o..o(8oo88"
            "888" 88"    888888888""
                o8P       "888"""
          ...oo88
 "8oo...oo888""
'''



def mprint():
    print(Colorate.Horizontal(Colors.red_to_green, Center.XCenter(ascii)))
    print()
    print(Colorate.Horizontal(Colors.red_to_green, Center.XCenter(f"Code: ({code})")))
    print('\n')

System.Size(140, 40)
Anime.Fade(Center.Center(flower), Colors.red_to_green, Colorate.Vertical, interval=0.025, enter=True)
print(Colorate.Horizontal(Colors.red_to_green, Center.XCenter(ascii)))
print('\n'*3)


server = "https://pandore.repl.co/"


code = Write.Input("Code -> ", Colors.green_to_red, interval=0.005)


def main():
    global code

    System.Clear()
    mprint()
    print(Colorate.Diagonal(Colors.red_to_green, Center.XCenter(modes)))
    print('\n'*2)
    mode = input(Col.red + "-" + Col.green + ">" + Col.reset + " ")
    System.Clear()
    mprint()

    if mode == '1':
        file = Write.Input("File -> ", Colors.green_to_red, interval=0.005)
        data = open(file, encoding='utf-8', errors='ignore').read()
        headers = {"code":code}
        r = post(server+'post', data=data.encode('utf-8'), headers=headers)
        print()
        input(Colorate.Diagonal(Colors.red_to_green, Center.XCenter(Box.DoubleCube(r.text))))
    elif mode == '2':
        headers = {"code":code}
        r = delete(server+'delete', headers=headers)
        print()
        input(Colorate.Diagonal(Colors.red_to_green, Center.XCenter(Box.DoubleCube(r.text))))
    elif mode == '3':
        code = Write.Input("Code -> ", Colors.green_to_red, interval=0.005)
        

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            Colorate.Error(str(e))
