#Name: [Redacted]
#StartDate: 10/10/17
#Date: 17/10/17
#Project: Interactive Novel

import time
import random
Response_Count = "True"
Inventory = "False"
Key = "False"
Cell_Count = "True"
Desk_Count = "True"
Cell_Desk = "True"
Cell_Desk2 = "True"
Cell_Note = "True"
Cell_Three = "False"
def Cell_Text():
    print("You awake in a dark dungeon, it's only a small cell but holds a bed, a desk and a hole in the floor")
    print("You faintly hear footsteps...")

Cell_Text()
Cell_Move = input("Where do you go first? (Check Bed or Check Desk): ").upper()
while Cell_Count == "True":
    if Cell_Move == "CHECK BED":
        print("You find a key in your pillow and stuff it in your pocket")
        print("+ silver key")
        Key = "Silver Key"
        Cell_Count = "False"
        Cell_Two = "CHECK BED"
    elif Cell_Move == "CHECK DESK":
        Cell_Two = "CHECK DESK"
        Cell_Three = "CHECK DESK"
        print("There's a padlock, maybe if you had a key...")
        Cell_Count = "False"
        if Key == "Silver Key":
            print("You use the key on the lock and look in the draw")
            time.sleep(1)
            print("There's a note")
            Note_Read = input("Do you read the note? ")
            while Desk_Count == "True":
                if Note_Read == "YES":
                    print("This key can unlock any door within the castle dungeon...dont get caught")
                    print("You hear footsteps heading towards your cell")
                    time.sleep(1)
                    print("You stuff the note in your pocket and sit down on the bed")
                    Inventory = "Note"
                    Desk_Count = "False"
                elif Note_Read == "NO":
                    print("You put the note in your pocket")
                    Inventory = "Note"
                    Desk_Count = "False"
                else:
                    print("yes or no please")
                    Note_Read = input("Do you read the note? ")
        else:
            Cell_Three = "CHECK DESK"
    else:
        print("Invalid Response...please go to the bed or desk (Check them)")
        Cell_Move = input("Where do you go first? (Check Bed or Check Desk ").upper()

while Cell_Desk == "True":
    if Cell_Two == "CHECK BED":
            print("You've found the key, now check out the desk")
            Cell_Desk = "False"
            Key = "Silver Key"
            if Key == "Silver Key":
                print("You use the key on the lock and look in the draw")
                time.sleep(1)
                print("There's a note")
                Note_Read = input("Do you read the note? ").upper()
                while Cell_Note == "True":
                    if Note_Read == "YES":
                        print("This key can unlock any door within the castle dungeon...dont get caught")
                        print("You hear footsteps heading towards your cell")
                        time.sleep(1)
                        print("You stuff the note in your pocket and sit down on the bed")
                        Inventory = "Note"
                        Cell_Desk = "False"
                        Cell_Note = "False"
                    elif Note_Read == "NO":
                        print("You put the note in your pocket")
                        Inventory = "Note"
                        Cell_Desk = "False"
                        Cell_Note = "False"
                    else:
                        print("yes or no please")
                        Note_Read = input("Do you read the note? ").upper()
    else:
        print("The bed might solve your answers...")
        time.sleep(1)
        print("you go to the bed")
        time.sleep(1)
        print("You find a key in your pillow and stuff it in your pocket")
        print("+ silver key")
        Key = "Silver Key"
        Cell_Desk = "False"
        Cell_Three = "CHECK DESK"
        Cell_Desk2 = "True"

if Cell_Three == "CHECK DESK":
    while Cell_Desk2 == "True":
        print("Let's go back to the desk")
        time.sleep(1)
        print("You go back to the desk...the sound of distant footsteps is heard")
        time.sleep(1)
        print("You use the key on the lock and look in the draw")
        time.sleep(1)
        print("There's a note")
        time.sleep(1)
        Note_Reads = input("Do you read the note? ").upper()
        while Cell_Note == "True":
            if Note_Reads == "YES":
                print("This key can unlock any door within the castle dungeon...dont get caught")
                print("You hear footsteps heading towards your cell")
                time.sleep(1)
                print("You stuff the note in your pocket and sit down on the bed")
                Inventory = "Note"
                Cell_Note = "False"
                Cell_Desk2 = "False"
            elif Note_Reads == "NO":
                print("You put the note in your pocket")
                Inventory = "Note"
                Cell_Note = "False"
                Cell_Desk2 = "False"
            else:
                print("yes or no please")
                Note_Read = input("Do you read the note? ").upper()
else:
    print("The footsteps grow nearer...and nearer")
    time.sleep(5)
print("Warden: Prisoner! Stand aside, by the desk!")
time.sleep(2)
print("You do as asked")
time.sleep(2)
print("The Warden unlocks the door and steps inside")
time.sleep(2)
print("Warden: What is your name!")
time.sleep(2)
Name = input("___: My name is ")
time.sleep(2)
print("Warden: Well",Name,"time for the block!")
time.sleep(2)
print("The Warden grabs you and throws you out of the cell")
time.sleep(2)
print("Warden: Get moving!")
time.sleep(2)
print("You walk along the corridors, hearing the moans and wails of other prisoners, you leave through a large wooden door")
time.sleep(2)
print("The sun blinds you, how long has it been since you have seen sunlight? Weeks? Months? It feels like them")
time.sleep(2)
print("You get thrown to the chopping block...the executioner raises his axe...")
time.sleep(5)
print("You pass out from exhaustion...a fire erupts from the building directly ahead of you...Everyone screams...")
time.sleep(15)
print("Strang: (in a hushed tone) Hey...wake up...",Name,"wake up! (They slap you awake)")
time.sleep(1)
print("(You awake..somehow alive)")
time.sleep(1)
print("(Not a scratch, not a mark)")
time.sleep(1)
print("Strang: hello...world to",Name)
time.sleep(1)
Response = input("(H..hi) (Hello...) (Hi there, and you are?) ").upper()
time.sleep(1)
while Response_Count == "True":
    if Response == "H..HI":
        print(Name+": H..hi")
        Response_Count = "False"
    elif Response == "HELLO...":
        print(Name+": Hello...")
        Response_Count = "False"
    elif Response == "HELLO THERE, AND YOU ARE?":
        print(Name+": Hello there, and you are?")
        Response_Count = "False"
    else:
        print("(Please pick one of the three choices)")
        Response = input("(H..hi) (Hello...) (Hi there, and you are?) ").upper()
time.sleep(1)
print("Stranger: finally...your'e awake")
time.sleep(2)
print("She steps off your body and stands aside")
time.sleep(2)
print("Stranger: Well...aren't you gonna ask my name?")
time.sleep(2)
print(Name+": Okay..what is your name...?")
time.sleep(2)
print("Stranger: That's for another day..let's go (She starts to walk off back towards the fort)")
time.sleep(2)
print(Name+": Hey..wait up!! (You get up and run to catch up)")
time.sleep(2)
print("Stranger: Well? Front door or sneaky entrance?")
time.sleep(2)
Response = input("(Front door)(Secret entrance)").upper()
print(Name+": let's go through the",Response)
Response_Count = "True"
while Response_Count == "True":
    if Response == "FRONT DOOR":
        print("You charge at the front door")
        print("Stranger: let's go...i guess")
        Response_Count = "False"
    elif Response == "SECRET ENTRANCE":
        print("Your'e a sneaky one, you take the back entrance")
        print("Stranger: okay, my kind of entrance")
        Response_Count = "False"
    else:
        Response = input("(Front door)(Secret entrance)").upper()
if Response == "FRONT DOOR":
    print("As you charge in, a guard turns the corner and sees you\nthey're about to alert the others\nwhat do you do? (Run)(Tackle)")
elif Response == "SECRET ENTRANCE":
    print("You sneak around the back and remove some foliage, you find a hole that has been mined out\nas you enter you see a guard staring right at you\nwhat do you do? (Charge)(Bargain)(run)")
time.sleep(2)
if Response == "FRONT DOOR":
    Response_Count = "True"
    Response = input("(Run)(Tackle) ").upper()
    while Response_Count == "True":
        if Response = "RUN":
            print
        elif Response = "TACKLE":
            print
        else:
            ptint("Incorrect response please pick (Run) or (Tackle)")
            Response = input("(Run)(Tackle) ").upper()
