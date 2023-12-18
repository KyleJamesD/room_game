from sys import exit

def gold_room():
    print ("This room is full of gold. How much do you take?")

    choice = input (">")
    if "abcdefnjkladefhweioqrioewqprjklFNZNCBVMNXZ" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print ("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy Person!!@")


def bear_room():
    print("There is a bear here.")
    print ("The bear has a bunch of honey.")
    print ("The fat bear is in front  of another door.")
    print ("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input (">")

        if choice == "take honey":
            dead("The bear looks at you and then slaps your face!")
        elif choice == "taunt bear" and not bear_moved:
            print ("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets angry and chews your leg!")
            start()
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print ("I got no idea what that means.")
            print("There is a bear here.")
            print ("The bear has a bunch of honey.")
            print ("The fat bear is in front of another door.")
            print ("How are you going to move the bear?")


def cthulu_room():
    print ("Here you see the great evil cthulu.")
    print ("He, it, whatevr stares at you and your hairs stand on end.")
    print ("Do you flee for your life or try to bargain?")

    choice = input (">")

    if "flee" in choice:
        start()
    elif "bargain" in choice:
        dead("Well that was easy!")
    else:
        cthulu_room()


def dead(why):
    print (why, "Good job!")
    start()

def start():
    print ("You are in a dark room.")
    print ("There is a door to your right and left.")
    print ("Which one do you take?")

    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room untill you starve.")
        start()


start()






    