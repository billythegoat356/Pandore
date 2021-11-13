from pystyle import *
from json import dump, load
from os import name, chdir

if name == 'nt':
    path = '/'.join(__file__.split('\\')[:-1])
    chdir(path)



# le JSON suivant contient des informations purement aléatoires

json = {
    "identity": {
        "name": "Thomas",
        "family_name": "Hauchard",
        "birth_date": "26/04/2002",
        "birth_place": "France",
        "age": "19",
    },

    "family_and_friends": [
        {
            "name": "Thomas",
            "family_name": "Hauchard",
            "birth_date": "26/04/2002",
            "birth_place": "France",
            "age": "19",
        },
        {
            "name": "Thomas",
            "family_name": "Hauchard",
            "birth_date": "26/04/2002",
            "birth_place": "France",
            "age": "19", 
        }
    ],

    "animals": [
        {
            "name": "Thomas",
            "family_name": "Hauchard",
            "birth_date": "26/04/2002",
            "birth_place": "France",
            "age": "19",
        },
        {
            "name": "Thomas",
            "family_name": "Hauchard",
            "birth_date": "26/04/2002",
            "birth_place": "France",
            "age": "19",
        }
    ],

    "hobbies": [
        "Football",
        "Skateboard"
    ],

    "food": [
        "Pizza",
        "Pasta",
        "Hamburger"
    ]
}


class mkwd:
    def mkwordlist(json: dict) -> list:
        wd = []
        id = [json['identity']]
        for element in json['family_and_friends']:
            id.append(element)
        for element in json['animals']:
            id.append(element)
        wd = []
        for x in id:
            for w in mkwd._processidentity(x, json['hobbies'], json['food']):
                wd.append(w)
        return wd

    def _processidentity(id: dict, hobbies: list, food: list) -> list:
        name = id['name']
        family_name = id['family_name']
        birth_date = id["birth_date"].split('/')
        birth_day, birth_month, birth_year = birth_date
        birth_place = id['birth_place']
        age = id['age']


        wd = []

        for a in (name, name+name, family_name):
            for x in (birth_day, birth_month, birth_year, age, birth_day+birth_month, birth_day+birth_month+birth_year):
                wd.append(a + x)
                wd.append(a.lower() + x)
                wd.append(x + a)
                wd.append(x + a.lower())

        for x in (birth_day, birth_month, birth_year, age, birth_day+birth_month, birth_day+birth_month+birth_year):
                wd.append(name + family_name + x)
                wd.append(name.lower() + family_name.lower() + x)
                wd.append(x + name + family_name)
                wd.append(x + name.lower() + family_name.lower())

        for a in (name, name+name, family_name):
            for x in (birth_day, birth_month, birth_year, age, birth_day+birth_month, birth_day+birth_month+birth_year):
                wd.append(a + x + "123")
                wd.append(a.lower() + x + "123")
                wd.append(x + a + "123")
                wd.append(x + a.lower() + "123")

        for a in (name, name+name, family_name):
            for x in food:
                wd.append(a + x)
                wd.append(a.lower() + x)
                wd.append(x + a)
                wd.append(x + a.lower())

        for a in (name, name+name, family_name):
            for x in food:
                wd.append(a + x + "123")
                wd.append(a.lower() + x + "123")
                wd.append(x + a + "123")
                wd.append(x + a.lower() + "123")

        for a in (name, name+name, family_name):
            for x in hobbies:
                wd.append(a + x)
                wd.append(a.lower() + x)
                wd.append(x + a)
                wd.append(x + a.lower())

        for a in (name, name+name, family_name):
            for x in hobbies:
                wd.append(a + x + "123")
                wd.append(a.lower() + x + "123")
                wd.append(x + a + "123")
                wd.append(x + a.lower() + "123")
        
        
        return wd



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

System.Size(140, 40)
System.Title("Pandore")
System.Clear()
Anime.Fade(Center.Center(flower), Colors.red_to_green, Colorate.Vertical, interval=0.025, enter=True)
print(Colorate.Horizontal(Colors.red_to_green, Center.XCenter(ascii)))
print('\n'*3)


with open('wordlist.json', mode='w', encoding='utf-8') as f:
    dump(json, f, indent=3)


Write.Input("A JSON file has been created in your actual folder.", Colors.green_to_red, interval=0.005)
print()
Write.Input("""Please complete it with the asked information, then press enter.""", Colors.green_to_red, interval=0.005)
print()
print()

def main():
    with open('wordlist.json', mode='r', encoding='utf-8') as f:
        json = load(f)
    Write.Input("The JSON dict has been succesfully loaded.", Colors.green_to_red, interval=0.005)
    print()
    wordlist = mkwd.mkwordlist(json)
    with open("wordlist.txt", mode='w', encoding='utf-8') as f:
        f.write("\n".join(wordlist))
    Write.Input(f"The wordlist has been created succesfully! The lenght is {len(wordlist)} lines and {sum(len(x) for x in wordlist)} characters.", Colors.green_to_red, interval=0.005)


        

if __name__ == '__main__':
    main()