print("enter the word you want to check for the palindrome" )
original = input("enter the original string:",) #take the user inputs
reverse_original = original[::-1] #reverse the original string
if original == reverse_original: #checks if original string matches the reverse string
    print(" it's a paindrome") #prints if it's a palindrome
elif original != reverse_original:
    print("it's not a palindrome") #prints if it's not a palindrome