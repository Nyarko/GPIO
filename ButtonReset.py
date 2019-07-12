from gpiozero import Button
from subprocess import call

button = Button(2)

n1 = int(input("Input your first number: "))
n2 = int(input("Now the next digit: "))

def print_thing():
    print ("Button pressed \n")
    print (evens(n1,n2))

def evens(n1,n2):
    
    while (n1 < (n2 - 1)):
        n1 = n1 + 1
        if (n1 % 2 == 0):
            print (n1)
    return 'Done'

print('The even numbers between', n1, 'and ', n2, 'are:')
print (evens(n1,n2))

print()

# import only system from os 
from os import system, name 

# import sleep to show output for some time period 
from time import sleep 

# define our clear function 
def clear(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# print out some text 
print('hello geeks\n'*10) 

# sleep for 2 seconds after printing output 
sleep(2) 

# now call function we defined above 
clear() 

button.when_pressed = print_thing
button.when_released = clear()