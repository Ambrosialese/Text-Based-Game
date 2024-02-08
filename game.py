import random
from msvcrt import getch
import time
import math
class player:
    def __init__(self, health, baseDamage):
        self.health = health
        self.baseDamage = baseDamage
playerStats = player(20, 6)
class enemy:
    def __init__(self, enemyType, health, baseDamage):
        self.enemyType = enemyType
        self.health = health
        self.baseDamage = baseDamage
def combat(playerHealth, playerDamage, enemyKind, enemyHealth, enemyDamage):
    print(f"You're currently in a stand off against {enemyKind}")
    print(f"{enemyKind} health = {enemyHealth}, your health = {playerHealth}")
    i = 1
    global winner
    while playerHealth > 0 and enemyHealth > 0:
        print(f"Turn {i}")
        answer = input("What would you like to do? Attack, Defend or Dodge")
        if playerHealth > 0 and enemyHealth > 0:
            if answer.lower() == "attack":
                damage = random.randrange(playerDamage - 3, playerDamage + 3)
                enemyHealth -= damage
                print(f"You've done {damage} damage to the {enemyKind}, they are now at {enemyHealth}")
                if i % 2 !=0:
                    takenDamage = random.randrange(enemyDamage - 1, enemyDamage + 1)
                    playerHealth -= takenDamage
                    print(f"{enemyKind} did {takenDamage} damage to you, you're now at {playerHealth}")
                else:
                    print("The opponent takes a moment to prepare themselves")
                i += 1
            elif answer.lower() == "defend":
                print("You hold up a defensive stance, halving the damage you take this turn")
                takenDamage = math.floor(random.randrange(enemyDamage - 1, enemyDamage + 1) / 2)
                playerHealth -= (takenDamage)
                print(f"{enemyKind} did {takenDamage} damage to you, you're now at {playerHealth}")
                i += 1
            elif answer.lower() == "dodge":
                print("you attempt to roll away")
                rollsuccess = random.randint(0,1)
                if rollsuccess == 1:
                    print("You've successfully rolled")
                    takenDamage = 0
                    playerHealth -= takenDamage
                    print(f"{enemyKind} did {takenDamage} damage to you, you're now at {playerHealth}")
                elif rollsuccess == 0:
                    print("you've stumbled and failed to roll properly")
                    takenDamage = random.randrange(enemyDamage - 1, enemyDamage + 1)
                    playerHealth -= takenDamage
                    print(f"{enemyKind} did {takenDamage} damage to you, you're now at {playerHealth}")
                i += 1
            else: 
                print("Sorry, I didn't understand that")
    if playerHealth <= 0:
        die_screen()
        winner = False
    elif enemyHealth <= 0:
        print(f"You've defeated the {enemyKind}")
        winner = True


def enter_building():
        print("Please enter the pin to gain access")
        id_number = input("Enter the ID number: ")
        if id_number.isdigit():
            print("Access granted! You successfully entered the building.")
            corridor()
        else:
            print("Invalid ID number. Access denied.")
            enter_building ()
def entry_method():
    global queenKey
    queenKey = False
    global greyBooksGet
    greyBooksGet = False
    answer = input("Enter 'stolen ID' or 'brute force': ")
    if answer.lower() == "stolen id":  # Using .lower() to handle case-insensitivity
        print("You decide to use a stolen ID to gain access.")
        enter_building()
    elif answer.lower() == "brute force":
        print ("you decide to fight your way in you run in with gun in your hand, shooting at anything that moves")
        shoot_out ()
    else:
        print ("sorry i dont understand, please try again")
        entry_method()
def shoot_out ():
    answer = input ("shoot 'receptionist' or 'security guard':")
    if answer.lower() == "receptionist":
        outcome = random.choices (["killed", "failed to kill"], weights = [0.8 , 0.2])
        print (f"you {outcome} the receptionist")
        if outcome == "killed":
            corridor ()
        else:
            cell()
    elif answer.lower () == "security guard":
        outcome = random.choices (["killed", "failed to kill"], weights = [0.2 , 0.8])
        print (f"you {outcome} the security guard")
        if outcome == "killed":
            corridor ()
        else:
            cell()
    else:
        print ("sorry i dont understand, please try again")
        shoot_out ()

def cell ():
    print ("you are in a prison cell strangely there is a combination alphabet lock on the inside (maybe the staff kept locking themselves in by mistake) and the  letters NEEUQ DRAZIL written aboved the door")
    answer = input  ("The cell is really boring the only thing is to try the lock, ENTER CODE:")
    if answer.lower () == ("lizard queen"):
        print ("you're out")
        corridor()
    else:
        print ("try again")
        cell()

def corridor():
    print ("You are in the corridor but you can barely move for lazer motion sensors you notice they are in the colours of the rainbow")
    print ("Just within reach there is a keypad on the wall, with four buttons: red, green, blue, and yellow. Next to the keypad, there is a sign that reads: Press the buttons in the correct order to unlock the door.")
    print ("This sign is sponsored by Skittles CAN YOU TASTE THE RAINBOW")
    colour1 = input ("enter colours in the correct order one at a time:")
    colour2 = input ("enter 2nd colour:")
    colour3 = input ("enter 3rd colour:")
    colour4 = input ("enter 4th colour:")
    if (colour1.lower() == "red") and (colour2.lower() == "yellow") and (colour3.lower() == "green") and (colour4.lower() == "blue"):
        print ("well done")
        hatchery()
    else:
        print ("try again")
        corridor()

def hatchery ():
    print ("You are in the a warm dry room you feel like you are in  a mothers embrace")
    print ("you hear a cracking noise, You see a three foot egg shaking")
    answer = input ("do you 'run' or 'search the room?'")
    if answer.lower() == ("run"):

        print ("Somehow you're now in a high security area")
        encounter()
    elif answer.lower() == ("search the room"):
        print ("you find a gun, this may come in handy")
        playerStats.baseDamage += 5
        new_born()
    else:
        print ("sorry i dont understand, please try again")
        hatchery()

def new_born():
    print("The shaking egg has an angry newborn lizard person, they're very aggressive when newly born so you have to fight!")
    newbornLizard = enemy("newborn", 30, 6)
    combat(playerStats.health, playerStats.baseDamage, newbornLizard.enemyType, newbornLizard.health, newbornLizard.baseDamage)
    if winner == True:
        print("After defeating the aggressive newborn, you continue onwards")
        encounter()

def encounter():
    print ("You bump into King Charles III.")
    print ("He talks to you about constitutional affairs and planning disputes in Gloucestershire.")
    print ("You try to ask him where his mum is but he seems unconserned like he's above it all.")
    print ("It all seems like a bit of a dead end!")
    print ("but then he mentions 'you'll need the key from the First Desk if I want to see her,")
    print ("I've been having to do that since the 8th September 2022")
    print("Charles wanders away, leaving you feeling confused. You continue onwards to another room")
    getch()
    officeBoss()
       
def dead_end ():
    print ("This is a dead end, go back")
    print("Press any key to continue")
    getch()
    hatchery()

def pin_lock():
    print ("Your outside the file room where the Grey Books are kept")
    print ("There is a pin pad lock on the door")
    print ("you find a piece of paper on the floor writen on it is 'don't forget when the queen was locked up'")
    answer = input ("enter pin code:")
    if answer.isdigit() == False:
        print ("enter numbers only")
        pin_lock()
    if answer == ("8922"):
        print ("You're in!")
        file_room()
    else:
        print ("try again and here's a clue the pin code is 4 digits long")
        pin_lock()

def file_room():
    print ("You open the door, its dark but the lights start to turn on automatically begining at the other end of the room, turning on one by one eventually illuminating you.")
    print ("The room is full of ordinary filing racks")
    file_room2()
def file_room2():
    answer = input ("There are three stand out items a 'treasure chest' a 'fridge' and a 'fire basket' which would you like to search?")
    if answer.lower() == ("treasure chest"):
        print ("You find gold bars this may change your life but isn't what you're looking for, you take as many as you can carry")
        file_room2()
    elif answer.lower() == ("fridge"):
        print ("You find a chicken mayo sandwich you wouldn't normally swipe someones lunch")
        print ("and you don't even like mayo but you havn't eaten in hours, you snaffle it and feel much better")
        file_room2()
    elif answer.lower() == ("fire basket"):
        print ("You find a file marked 'The Grey Books' looks like it was going to be incinerated and you've got here just in time")
        greyBooksGet = True
        print ("One last light flickers on, its the emergency exit! as the green glow envelopes you, you approach the door")
        print ("there's a big lever on the door accross it the legend 'Push to Exit' is engraved:")
        leave = input("Do you want to leave with just this evidence?")
        if leave.lower() == "yes":
            print("Yeah, Surely this evidence will be enough to allow another larger scale rescue of her later. You leave by yourself.")
            escape_alone_with_evidence()
        elif leave.lower() == "no":
            print("Your determination to save the Queen hasn't wavered, this will be excellent to bring out with her.")
            print("You leave the file room to go back and try save her")
            look_around()
    else:
        print ("sorry I don't  understand")
        file_room2 ()

def escape_alone_with_evidence():
      print(r"""\

     ___
 ___/   \___
/   '---'   \
'--_______--'
     / \
    /   \
    /\O/\
    / | \
    // \\


                """)
      print(r"""\
           
      <>              
    .::::.            
@\\/W\/\/W\//@        
 \\/^\/\/^\//    
  \_O_<>_O_/
                            """)
      print("Congratulations! You have managed to escape with evidence of government conspiracy, The Queen is still locked up in there but in the future surely she will be saved, right?")
      print("Scroll up for cool ASCII art!")

def escape_with_evidence():
      print(r"""\

     ___
 ___/   \___
/   '---'   \
'--_______--'
     / \
    /   \
    /\O/\
    / | \
    // \\


                """)
      print(r"""\
           
      <>              
    .::::.            
@\\/W\/\/W\//@        
 \\/^\/\/^\//    
  \_O_<>_O_/
                            """)
      print("Congratulations! the Queen is free and you have evidence proving the existence of government conspiracies")
      print("Scroll up for cool ASCII art!")

def grab_queen():
    print("You look around the room and spot the Queen!")
    user_choice = input("The Queen asks if you are here to save her. Type 'yes' or 'yes and the grey books' to save her: ").lower()
    if user_choice == "yes":
        win()
    elif user_choice == "yes and the grey books":
        if greyBooksGet == True:
            escape_with_evidence()
        else:
            print("she says `You clearly don't, thanks for the escape route but this treason cannot go unpunished`")
            print("The queen eats you")
            getch
            dead_win()
    else:
         print ("that was a lot of effort for nothing")
         print ("The queen eats you")
         print ("Press any key to continue")
         getch()
         die_screen()

def officeBoss():
    Boss = enemy("The Boss", 45, 8)
    print("You get noticed quickly from the sound of the door opening, the man on the opposite side of the room turns around quickly and pulls out a gun to attack")
    combat(playerStats.health, playerStats.baseDamage, Boss.enemyType, Boss.health, Boss.baseDamage)
    if winner == True:
        print("With the boss' body slumping to the floor, you search the desk and find a key with a tag labelled `Queen Room` which you pick up, You also notice on the screen some text mentioning the destruction of `grey books` in the file room nearby.")
        global queenKey
        queenKey = True
        print("You become interested in these `grey books`, do you want to go search for them?") 
        decision = input("yes or no?")
        if decision.lower() == "yes":
            pin_lock()
        elif decision.lower() == "no":
            look_around()
        else:
            print("please enter a valid answer")
    

def die_screen():
    print("""
### ##     ####   ### ###  
 ##  ##     ##     ##  ##  
 ##  ##     ##     ##      
 ##  ##     ##     ## ##  
 ##  ##     ##     ##      
 ##  ##     ##     ##  ##  
### ##     ####   ### ###                      
""")
    print("You are dead along with the Queen's hope of being rescued. Better luck next time.")
    
def dead_win():
    print("""
### ##     ####   ### ###  
 ##  ##     ##     ##  ##  
 ##  ##     ##     ##      
 ##  ##     ##     ## ##  
 ##  ##     ##     ##      
 ##  ##     ##     ##  ##  
### ##     ####   ### ###                      
""")
    print("You are dead, although you've managed to allow the queen to escape, so... a winner is you?")

def look_around():
    print("You look around the office...")
    time.sleep(3)
    print("A painting on the wall captures your attention.")
    if input("Do you want to inspect the painting closer? (yes): ").lower() == "yes":
        print("The framed painting is noticeably uneven and leaning to the right.")
        print("This looks unusual!")
        if input("Do you want to take the frame off the wall to adjust it? (yes): ").lower() == "yes":
            print("You take the painting off the wall revealing a hidden golden key.")
            if input("Do you want to take the key? (yes): ").lower() == "yes":
                print("You take the key. It looks like a perfect match for the door over there!")
                next_step = True

            else:
                print("You leave the key behind.")
                next_step = False
        else:
            print("You leave the painting on the wall.")
            next_step = False
    else:
        print("You continue looking around.")
        next_step = False
    print("You are in the office.")
    if next_step == True:
        open_door()
    else:
        print ("You are discovered")
        die_screen ()

def open_door():
    print("You see a door in front of you in this office")
    if queenKey == True:
        if input("Do you want to try using the key you found in the boss' office to open the door? (yes): ").lower() == "yes":
            print("You insert the key into the door's lock and turn it. It works!")
            print("The door unlocks revealing the Queen laid on the floor with her arms and legs bound by rope.")
            grab_queen()
        else:
            print("You decide not to try the key on the door.")
            die_screen()
    else:
        print("You don't have a matching key for this, you need to find it... but you get discovered!")
        die_screen()
        

     

def win():
    print('''
    \ \        / /|_   _|| \ | |
    \ \  /\  / /   | |  |  \| |
    \ \/  \/ /    | |  | . ` |
      \  /\  /    _| |_ | |\  |
       \/  \/    |_____||_| \_|                                          
    ''')

    time.sleep(2)

    print("You win! Congratulations, you saved the Queen and restored peace!")

print("You have the choice to enter the MI5 Headquarters using a stolen ID or by using brute force")
print("Which choice will you take?")

entry_method()
