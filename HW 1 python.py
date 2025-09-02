#Sections 1&2 conditionals with input
'''
name= input("what is your name: ")
print (f"your name is {name}")
age = int(input("what is your age:"))
print(f"Hello, {name}")
print(f"you are {age} years old")
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")##
'''
#Section 3 Loops with input
'''
for i in range (5):
   score = int(input(f"enter score {str(i+1)}: "))
   print(f"You entered: {score}")
'''
#Section 5: While loops with input
'''
num = int(input("enter a positive #"))
tries = 0
while num <0 :
    print("thats not positive dumbass")
    num = int(input ("enter a positive number:"))
    tries + 1
    if tries > 5:
        print ('js give up')
'''
#Challenges: grading program
i = 0
scores = int(input(f"Grade # {i}"))
print("To end program ans see class average, enter a negative number") 
db = []
while scores > 0 :
    i+1
    scores=int(input(f"Grade # {i}"))
    print(scores)
    db.append(scores)
print(db)
