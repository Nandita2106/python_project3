import random
computer=random.choice([-1,0,1])
print("Welcome to Rock, Paper, Scissors!")
print("Choose 'rock', 'paper', 'scissor' to play.")
print("Type 'quit' to stop playing")
while True:
 youstr=input("enter your choice:")
 if youstr not in ['rock', 'paper', 'scissor']:
  print("Invalid choice. Please try again!")
  continue 
 youdict = {"rock" : 1, "paper": -1, "scissor": 0}
 reversedict={1: "rock", -1: "paper", 0:"scissor"}
 you= youdict[youstr]

 print(f"your choice: {reversedict[you]}\nComputer choice: {reversedict[computer]}")


 if(computer==you):

    print("it's a draw!")

 else:
    
   if(computer ==-1 and you==1):
    print("You lose!")

   elif(computer== -1 and you==0):
    print("You win!")


   elif(computer==1 and you==-1):
    print("You win!")

   elif(computer==1 and you==0):
    print("You lose!")

   elif(computer==0 and you==1):
    print("You win!")

   elif(computer==0 and you==-1):
    print("You lose!")            

   else:
    print("something went wrong!")

 play_again = input("Do you want to play again? (yes/no): ").lower()
 if play_again != 'yes':
  print("Thanks for playing! Goodbye.")
  break
