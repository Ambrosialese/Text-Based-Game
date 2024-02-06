
import random
def enter_building():
        print("Please enter the pin to gain access")
        id_number = input("Enter the ID number: ")
        if id_number.isdigit():
            print("Access granted! You successfully entered the building.")
        else:
            print("Invalid ID number. Access denied.")
def entry_method():
    answer = input("Enter 'stolen ID' or 'brute force': ")
    if answer.lower() == "stolen id":  # Using .lower() to handle case-insensitivity
        print("You decide to use a stolen ID to gain access.")
        enter_building()
    elif answer.lower() == "brute force":
        print ("you decide to fight your way in you run in with gun in your hand, shooting at anything that moves")
    else:
        print ("sorry i dont understand, please try again")
        entry_method()
def shoot_out ():
        answer = input ("shoot 'receptionist' or 'security guard':")
        if answer.lower() == "receptionist":
            outcome = random.choices (["killed", "failed to kill"], weights = [0.8 , 0.2])
            print (f"you {outcome} the receptionist")
        elif answer.lower () == "security guard":
            outcome = random.choices (["killed", "failed to kill"], weights = [0.2 , 0.8])
            print (f"you {outcome} the security guard")
        else:
            print ("sorry i dont understand, please try again")
            shoot_out ()

def cell ():
            print ("you are in a prison cell strangely there is a combination alphabet lock on the inside (maybe the staff kept locking themselves in by mistake) and the  letters NEEUQ DRAZIL written aboved the door")
            answer = input  ("The cell is really boring the only thing is to try the lock")
            if answer.lower () == ("lizard queen"):
                print ("your out")
            else:
                 print ("try again")
                 cell ()



print("You have the choice to enter the MI5 Headquarters using a stolen ID or by using brute force")
print("Which choice will you take?")

entry_method()
shoot_out ()    
cell()
