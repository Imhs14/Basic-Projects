import random
while True:
    choice = input("Roll dice!(y/n)").lower()
    if choice == 'y':
        die1 = random.randint(1,6) #gives random input to dice 1
        die2 = random.randint(1,6) # gives random input to dice 2
        print( die1,die2)
    elif choice == 'n':
        print("Thanks for playing") 
        break
    else:
        print("invalid input")