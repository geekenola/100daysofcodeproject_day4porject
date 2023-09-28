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

#Write your code below this line 👇
print(rock + "\n" + paper + "\n" + scissors)
arr=[rock, paper, scissors]
user_choice=int(input("Enter the number of your sign 0-rock,1- paper, 2-scissors"))
comp_sign = random.randint(0,2)
if user_choice>>2 or user_choice<0:
   print("You typed an invalaid number, you lose!")
elif user_choice == 0 and comp_sign == 2:
  print(f"You chose {arr[0]} and computer chose {arr[2]}")
  print("You win!")
elif user_choice > comp_sign:
  print(f"You chose {arr[user_choice]} and computer chose {arr[comp_sign]}! ")
  print("You win!")
elif user_choice == comp_sign:
   print(f"You both chose {arr[user_choice]}")
   print("DRAW")
else:
    print(f"You chose {arr[user_choice]} and computer chose {arr[comp_sign]}! ")

    print("Computer wins!")
