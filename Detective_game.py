import random
print("Hello detective we got some fugitives for u")
targets = [  {"name":"Mayor vance",
            "crime":["Embezzelment","fraud"],
            "threat_level":random.randint(1,10),
            "caught":False},
           {"name":"Victor sterling",
             "crime":["Money laundering","Bribery"],
             "threat_level":random.randint(1,10),
             "caught":False},
           {"name":"John",
            "crime":["illegal casino","Drug seller"],
            "threat_level":random.randint(1,10),
            "caught":False}
]
             
user_intp = input("Enter a target name: ")
for t in targets:
    if user_intp.lower() in t["name"].lower():
        print("Crime:",t["crime"])
        print("threat level:",t["threat_level"])
        print("Is he caught:",t["caught"])
        user_ques = input("Did you manage to catch him?:(yes/no)").lower()
        if user_ques == "yes":
            ok = t["caught"] = True
            print("Caught:",ok)
            print("Congrats detective")
        elif user_ques == "no":
            print("Try again")
        else:
            print("Must be  typo?")
