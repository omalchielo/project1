'''
author = Michal Hradil
'''
TEXT1 = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''']

TEXT2= ['''
At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.'''
]

TEXT3= ['''
The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]


login = {"bob":"123","ann":"pass123","mike":"password123","liz":"pass123"}

name = input("Zadej sve jmeno: ")
password = input("Zadej sve heslo: ")
if name in login.keys() and password == login.get(name):
    print("-"*50,f"Welcome to the app, {name}","We have 3 texts to be analyzed.","-"*50,sep="\n")
    number = input("Enter a number btw. 1 and 3 to select: ")
    if number == "1":
        cislo = TEXT1
    elif number =="2":
        cislo = TEXT2
    elif number =="3":
        cislo = TEXT3
    else:
        print("-"*50,"Spatny vstup!","-"*50,sep="\n")
        quit()

    string = "".join(cislo)



    text = string.split()
    pocet_slov = len(text)

    velka_pismena = 0
    vsechny_velke = 0
    vsechny_male = 0
    vsechny_cisla = 0
    pocet = 0
    delka1 = []
    for pismeno in text:
        if pismeno.istitle():
            velka_pismena+=1
        elif pismeno.isupper():
            vsechny_velke+=1
        elif pismeno.islower():
            vsechny_male+=1
        elif pismeno.isnumeric():
            vsechny_cisla+=1
            pocet+=int(pismeno)


    text = string.replace(",","").replace(".","").split()

    for pismeno in text:
        delka = len(pismeno)
        delka1.append(delka)



    print(f"There are {pocet_slov} words in the selected text.")
    print(f"There are {velka_pismena} titlecase words.")
    print(f"There are {vsechny_velke} uppercase words.")
    print(f"There are {vsechny_male} lowercase words.")
    print(f"There are {vsechny_cisla} numeric strings.")
    print(f"The sum of all the numbers {pocet}")
    a = 0
    maximum = max(delka1)
    for cislo in range(a,maximum):
        a += 1
        delka2 = delka1.count(a)
        mezera = 20 -  delka2
        space = 1
        if a == 1:
            print("-"*50)
            print("{:>5}".format("LEN  |"),"{:>17}".format("OCCURENCES"),"{:>9}".format("| NR."))
            print("-"*50)
        if a > 9:
            space = 0
        print(" "*space,a," |", "*" * delka2," "*mezera, "|", delka2)


else:
    print("Nepsprávné jméno nebo heslo")
    quit()

