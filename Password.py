#reads the passowrd.txt file to get the external passowrd and assigns it to the variable "name"
with open("password.txt") as f:
    name = f.read()
    #print(name)

#sets variable for number of available tries
tries = 5  
#Begins the while loop until tries reaches 0
while tries > 0:
    
#calls for and assigns user input as "x"
    x = input("Enter Password: ")
    
#Compares the input stored in "x" to the password stored in "name",
#if correct prints "correct" then stops the loop    
    if x == name:
        print("correct")
        break
    
#compares the input stored in "x" to the password stored in "name",
#if true prints "out of tries" signalling the end of the loop and locking user out. 
    if tries == 1:
        print("Out of tries")
        break
                   
#if incorrect, reduces tries by 1 and asks for input again for the next try.
    else:
        print("incorrect")   
        tries -= 1
        print("Tries left:",tries)



