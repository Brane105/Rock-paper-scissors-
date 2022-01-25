import random 
print("Welcome to rock paper scissors game !")
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
print("ROCK = 0")
# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
print("Paper = 1")
# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print("Scissors = 2\n")

hand = int(input("what do you choose ? type 0 for ROCK , 1 for Paper and 2 for Scissors : "))

print("You choose :")
if hand == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif hand == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif hand == 2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else :
    print("Invalid input")

comp = random.randint(0,2)
print("Computer choose : ")
if comp == 0:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif comp == 1:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif comp == 2:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
if hand == 0 and comp == 2:
    print("you won !")
elif hand == 2 and comp == 0: 
    print("you lost ! ")
elif hand == 1 and comp == 2:
    print("You lost !")
elif hand == 2 and comp == 1:
    print("You Won !")
elif hand == 1 and comp == 0:
    print("You Lost !")
elif hand == 0 and comp == 1:
    print("You Won !")
elif hand == comp:
    print("Draw !")