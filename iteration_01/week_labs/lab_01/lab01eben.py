running = True      
while running:
    username  = input("What is your name ")
    print(f"Hello {username}")
    age = int(input((f"{username}, how old are you?")))
    if age < 13:
        print("You can't sit in the passenger seat of a car, you can't vote, and you can't rent a car. On the plus side, you're not getting old. Yet.")
    elif age < 18:
        print("You still can't vote or rent a car, but at leat you're still young.")
    elif age < 25:
        print("You're getting up in years, unc. You still can't rent a car, though.")
    elif age > 35:
        print("Pack it up, grandpa. They're ready over at the nursing home.")
    else: 
        print("It's whatever, man.")
    langs = []
    langslearn = []
    userinfo = {
        "Name" : username,
        "Age" : age,
        "Languages Spoken" : langs,
    }
    languagestatus = input("Are you multilingual (yes/no)? ")
    if languagestatus == "yes":
        language = input("What is a language you speak? ")
        langs.append(language)
    else:
        languagelearn = input("What is a language you want to learn? ")
        langslearn.append(languagelearn)
        
    print(userinfo)
    runtime = input("Would you like to add another user (y/n)? ")
    if runtime == "yes" :
        running = True
    else: 
        running = False




    
    

