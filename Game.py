ComChoices = ("rock","paper","scissor")
import  random 

def RPS():
    while True:
        Comp = random.choice(ComChoices)
        Player = input("Enter your choice(Rock, Paper, Scissor,Exit : ").strip().lower()
        if Player not in ("rock", "paper", "scissor","exit"):
            continue
        if Player == "exit":
            print("Thank you for playing")
            break
        if Player == "rock" and Comp == "paper":
            print("Comp Win!")
            RPS()
        elif Player == "scissor" and Comp == "rock":
            print("Comp Win!")
            RPS()
        elif Player == "paper" and Comp == "scissor":
            print("Comp Win!")
            RPS()
        else:
            print("Player Win!")
            RPS()

while True:
  print("\t\t\tWelcome to Rock Paper Scissor Game\n")
  inout=input("___y/n___:")
  if inout.strip().lower() == "y":
    RPS()
    break
  elif inout.strip().lower() == "n":
    print("Thank you for visiting")
    break
  else:
     continue