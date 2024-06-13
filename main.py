import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''




choose_sign = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n")
if choose_sign == "0":
    print(rock)
elif choose_sign == "1":
    print(paper)
elif choose_sign == "2":
    print(scissors)

computer_choose = random.randint(0, 2)
if computer_choose == 0:
    print(rock)
elif computer_choose == 1:
    print(paper)
elif computer_choose == 2:
    print(scissors)

if (choose_sign == "0") and (computer_choose == 2):
    print("U Win")
elif (choose_sign == "0") and (computer_choose == 0):
    print("Draw")
elif (choose_sign == "0") and (computer_choose == 1):
    print("U Lose")

if (choose_sign == "1") and (computer_choose == 0):
    print("U Win")
elif (choose_sign == "1") and (computer_choose == 1):
    print("Draw")
elif (choose_sign == "1") and (computer_choose == 2):
    print("U Lose")

if (choose_sign == "2") and (computer_choose == 1):
    print("U Win")
elif (choose_sign == "2") and (computer_choose == 2):
    print("Draw")
elif (choose_sign == "2") and (computer_choose == 0):
    print("U Lose")
