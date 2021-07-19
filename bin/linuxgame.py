print(" ________")
print("| |____| |")
print("|   __   |")
print("|  (__)  |")
print("|________|")
print("\nLoading Game...")
import random
yes = ""
no = ""

def dragon():
    print("Beta 0.1.5")
    print("   (  )   /\   _                 (     ")
    print("    \ |  (  \ ( \.(               )                      _____ ")
    print("  \  \ \  `  `   ) \             (  ___                 / _   \ ")
    print(" (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_ ")
    print("- .-               \+  ;          (  O                           \____ ")
    print("                          )        \_____________  `              \  / ")
    print("(__                +- .( -'.- <. - _  VVVVVVV VV V\                 \/ ")
    print("(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  | ")
    print("  .    /./.+-  . .- /  +--  - .     \______________//_              \_______ ")
    print("  (__ ' /x  / x _/ (                                  \___'          \     / ")
    print(" , x / ( '  . / .  /                                      |           \   / ")
    print("    /  /  _/ /    +                                      /              \/ ")
    print("   '  (__/                                             /                  \ \n")

def newscreen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def startscreen():
    print
    newscreen()
    dragon()
    game = input("Do you wish to start the game? (yes, no): ")
    if game == "yes":
        newscreen()
        print(game)
        #gamesetup
    elif game == "no":
        newscreen()
        dragon()
        print("Thanks for playing")
        quit()
    else:
        newscreen()
        startscreen()
startscreen()