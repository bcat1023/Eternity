print(" ________")
print("| |____| |")
print("|   __   |")
print("|  (__)  |")
print("|________|")
print("\nLoading Game...")

# Setting vales
st = "True"
yes = ""
no = ""
gm = "False"
prmtut = "True"
setuploop = "True"
game = "True"

def dragon():
    print("Beta 0.2.5")
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

def skip():
    print("")

def gameclose():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    dragon()
    input("Thanks for playing, press enter to quit")
    quit()

def gamestart():
  while game:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to Eternity")
    print(" ________")
    print("| |____| |")
    print("|   __   |")
    print("|  (__)  |")
    print("|________|")
    print("\nLoading Game...")
    #importing modules
    import random
    health = 100
    day = "Monday"
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Brandon " + str(health) + str("HP") + str(", Its " + str(day)))
    activity = input("What do you want to do? (Look for a fight, Visit healers, Quit)")
    if activity == "Visit healers":
        print("\nThis feature should come in the next version of the game")
        input("Press enter to continue")
    if activity == "Quit":
        gameclose()
    if activity == "Look for a fight":
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to Eternity")
      print(" ________")
      print("| |____| |")
      print("|   __   |")
      print("|  (__)  |")
      print("|________|")
      print("\nLoading Area...")
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLooking for a fight...")
      fightnum = random.randint(1, 1)
      if fightnum == 1:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to Eternity")
        print(" ________")
        print("| |____| |")
        print("|   __   |")
        print("|  (__)  |")
        print("|________|")
        print("\nLoading Fight...")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou have found a old turtle")
        print("Turtle's HP: 15HP, Your HP " + str(health))
        fightsus = input("Do you want to fight the Turtle? (yes, no)")
        if fightsus == "yes":
          anhealth = 15
          print("\n\n\nTurtle hits you")
          print("You have lost 5HP")
          print("Turtle HP is" + str(anhealth))
          print("You hit Turtle for 5HP")
          anhealth = 10
          print("Turtle hits you")
          print("You have lost 5HP")
          print("Turtle HP is" + str(anhealth))
          print("You hit Turtle for 5HP")
          anhealth = 5
          print("Turtle hits you")
          print("You have lost 5HP")
          print("Turtle HP is" + str(anhealth))
          print("You hit Turtle for 5HP")
          anhealth = 0
          print("You have killed Turtle and gained 10HP from Turtle")
          #addcodehere
          input("Press any enter to go back")
        else:
          print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to Eternity")
          print(" ________")
          print("| |____| |")
          print("|   __   |")
          print("|  (__)  |")
          print("|________|")
          print("\nLoading Menu...")
      else:
        print("error check 1")
    else:
        skip()
#setup
def setup():
  while setuploop:
    gm = "False"
    st = "False"
    charname = input("What do you want your name to be: ")
    chargen = input("Pick a gender (male, female, other): ")
    setupcomfin = "True"
    while setupcomfin:
      print("\n\n\n\n\n\n\n\n\n\nPlease check that this is what you want")
      charconfirm = input("Are you sure you want your name to be " + str(charname) + str("\nAnd your gender to be ") + str(chargen) + str("? (yes, no): "))
      if charconfirm == "yes":
        print("Alright then, Lets get started")
        gamestart()
        setupcomfin = "False"
      elif charconfirm == "no":
        print("Ok then, you can change it")
        setup()
      else:
        print("Invalid Input")
while st:
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to Eternity")
  dragon()
  game = input("Do you wish to start the game? (yes, no): ")
  if game == "yes":
    gm = "True"
    st = "False"
  elif game == "no":
    gameclose()
  else:
    print("Unexpected input")
  
  while gm:
    returnpromt = input("\nWelcome to Eternity, Lets get started\nHave you played eternity before? (yes, no): ")
    if returnpromt == "yes":
      print("\n\nGreat lets get started")
      setup()
    elif returnpromt == "no":
      while prmtut:
        print("\nGreat lets start the tutorial\nPromts will come at you in a special format like this\nquestion (Possible, answers):")
        promttut = input("Here is an example, do you understand the format yet? (yes, no): ")
        if promttut == "no":
          print("Thats ok, we can do it again")
        elif promttut == "yes":
          print("Great, lets get started then")
          setup()
          gm = "False"
          st = "False"
print("end of code, stop 1")
